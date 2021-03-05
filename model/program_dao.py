from sqlalchemy import text

class ProgramDao:
    def __init__(self, database):
        self.db=database

    def get_boot_camp_id(self, camp_name):
        return self.db.execute(text("""
            SELECT *
            FROM boot_camps
            WHERE name=:camp_name
        """),{'camp_name':camp_name}).rowcount

    def get_filters(self):
        tags=self.db.execute(text("""
            SELECT name
            FROM tags
        """)).fetchall()
        tag_list=[tag['name'] for tag in tags]

        return tag_list

    def get_programs(self, boot_camp_id):
        programs=self.db.execute(text("""
            SELECT p.id, p.boot_camp_id, p.name as program_name, 
            p.program_total_score, p.cost, p.eng_name,
            b.logo_url, b.kor_name, b.name as camp_name
            FROM camp_programs p
            LEFT JOIN boot_camps b ON b.id=:boot_camp_id
            WHERE p.boot_camp_id=:boot_camp_id
        """),{'boot_camp_id':boot_camp_id}).fetchall()
        
        program_list=[]

        for p in programs:
            program={}
            program['id']=p['id']
            program['bootcampName']=p['camp_name']
            program['bootcampNameKor']=p['kor_name']
            program['courseName']=p['eng_name']
            program['courseNameKor']=p['program_name']
            program['score']=p['program_total_score']
            program['logoUrl']=p['logo_url']
            program['price']=p['cost']

            tags=self.db.execute(text("""
                SELECT id, name
                FROM tags
                WHERE id in (
                    SELECT tag_id
                    FROM camp_program_tags
                    WHERE camp_program_id=:program_id
                )
            """),{'program_id':p['id']}).fetchall()
            
            program['tags']=[tag['name'] for tag in tags]

            program_list.append(program)
        
        return program_list

    def get_program_detail(self, program_id):
        detail=self.db.execute(text("""
            SELECT id, name, eng_name, intro, detail, cost,
            operating_time, students, program_total_score
            FROM camp_programs
            WHERE id=:program_id
        """),{'program_id':program_id}).fetchone()

        tag=self.db.execute(text("""
            SELECT id, name
            FROM tags
            WHERE id=(
                SELECT tag_id
                FROM camp_program_tags
                WHERE camp_program_id=:program_id 
                AND (tag_id=6 OR tag_id=7)
            )
        """),{'program_id':program_id}).fetchone()

        return {
            'id':program_id,
            'courseName':detail['eng_name'],
            'courseNameKor':detail['name'],
            'intro':detail['intro'],
            'curriculum':detail['detail'],
            'price':detail['cost'],
            'operationTime':detail['operating_time'],
            'onlineOffline':tag['name'],
            'students':detail['students'],
            'score':detail['program_total_score']
        }

    def get_program_comment(self, program_id):
        comments=self.db.execute(text("""
            SELECT c.id, c.camp_program_id, c.user_id, c.content, 
            c.recomment_id, u.name
            FROM comments c
            LEFT JOIN users u ON u.id=user_id
            WHERE camp_program_id=:program_id
        """),{'program_id':program_id}).fetchall()

        comment_list=[]
        
        for c in comments:
            comment={}
            comment['id']=c['id']
            comment['userId']=c['user_id']
            comment['userName']=c['name']
            comment['content']=c['content']
            comment['recomment']=[]

            if c['recomment_id']:
                for rc in comment_list:
                    if rc['id']==c['recomment_id']:
                        rc['recomment'].append(comment)
            else:
                comment_list.append(comment)
        
        return comment_list
                

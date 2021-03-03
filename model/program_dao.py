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

            
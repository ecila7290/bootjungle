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

    def get_programs(self, boot_camp_id):
        programs=self.db.execute(text("""
            SELECT p.id, p.boot_camp_id, p.name, p.program_total_score, b.logo_url
            FROM camp_programs p
            LEFT JOIN boot_camps b ON b.id=:boot_camp_id
            WHERE p.boot_camp_id=:boot_camp_id
        """),{'boot_camp_id':boot_camp_id}).fetchall()

        program_list={'programs':[]}

        for p in programs:
            program={}
            program['programId']=p['id']
            program['name']=p['name']
            program['score']=p['program_total_score']
            program['logoUrl']=p['logo_url']

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

            program_list['programs'].append(program)
        
        return program_list

            
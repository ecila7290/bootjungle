class ProgramService:
    def __init__(self, program_dao):
        self.program_dao=program_dao
    
    def get_boot_camp_id(self, boot_camp_name):
        return self.program_dao.get_boot_camp_id(boot_camp_name)

    def get_filters(self):
        return self.program_dao.get_filters()
        
    def get_programs(self, boot_camp_name):
        boot_camp_id=self.get_boot_camp_id(boot_camp_name)
        return self.program_dao.get_programs(boot_camp_id)

    def get_program_detail(self, program_id):
        return self.program_dao.get_program_detail(program_id)

    def get_program_comment(self, program_id):
        return self.program_dao.get_program_comment(program_id)
    
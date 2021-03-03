class ProgramService:
    def __init__(self, program_dao):
        self.program_dao=program_dao
    
    def get_boot_camp_id(self, boot_camp_name):
        return self.program_dao.get_boot_camp_id(boot_camp_name)

    def get_programs(self, boot_camp_name):
        boot_camp_id=self.get_boot_camp_id(boot_camp_name)
        return self.program_dao.get_programs(boot_camp_id)
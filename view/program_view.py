from flask import Flask, jsonify, request

class ProgramView:
    def create_endpoints(app, services):
        program_service=services.program_service

        @app.route('/api/bootcamp/<string:camp_name>', methods=['GET'])
        def programs(camp_name):
            camp_id=program_service.get_boot_camp_id(camp_name)
            programs=program_service.get_programs(camp_name)

            return jsonify({
                'bootCampId':camp_id,
                'programs':programs
            })
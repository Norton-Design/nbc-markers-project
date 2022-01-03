import re
import datetime

class Marker:
    TEST_FILE_PATH = './test/sample.txt'

    @classmethod
    def validate_markers_file(self, file):
        # process file and return json of the validation
        result = self.process_markers_file(file)
        if result['is_valid']:
            return result
        else:
            return {""} # <----- Come back to this

    @classmethod
    def process_markers_file(self, file):
        processed_lines = []
        with open(file, 'r') as f:
            lines = f.readlines()
            lines = [line.rstrip() for line in lines]
            for line in lines:
                # prompt indicates that txt will only ever be one line long but
                # from a working standpoint, I think we can cover multiline files
                # with minimal effort
                processed_lines.append(self.process_text_line(line))
        if len(processed_lines) == 1:
            return processed_lines[0]
        elif len(processed_lines) == 0:
            return { 'is_valid': False, "message": "No processable lines" }
        else:
            # Come back and handle multiple line solution
            pass

    @classmethod
    def process_text_line(self, line):
        processed_data = {}
        section_list = line.rstrip().split("   ")
        asset_title, asset_id, material_type, date, *markers = section_list
        if self.validate_asset_title(asset_title):
            processed_data['asset_title'] = asset_title
        if self.validate_asset_id(asset_id):
            processed_data['asset_id'] = asset_id
        if self.validate_material_type(material_type):
            processed_data['material_type'] = material_type
        if self.validate_date(date):
            processed_data['date'] = date
        if self.validate_timecode_markers(markers):
            processed_data['markers'] = self.process_timecode_markers(markers)
        return processed_data

    @classmethod
    def process_timecode_markers(self, timecode_markers):
        paired_codes = []
        for i in range(0, len(timecode_markers), 2):
            in_code = timecode_markers[i]
            out_code = timecode_markers[i+1]
            paired_codes.append((in_code, out_code))
        return paired_codes

    @classmethod
    def validate_asset_title(self, title):
        return len(title) <= 100 and len(title) >= 1

    @classmethod
    def validate_asset_id(self, id):
        pattern = re.compile(r'[A-Z]{4}[0-9]{9}')
        return pattern.match(id) and len(id) == 13

    @classmethod
    def validate_material_type(self, type):
        # Deviates from the prompt here to be consistant with the sample input. Added "news" as valid
        return type in ['movie', 'episode', 'sports', 'news']

    @classmethod
    def validate_date(self, date):
        # Check back about this one
        try:
            datetime.datetime.strptime(date, '%m-%d-%Y')
        except ValueError:
            raise ValueError('Incorrect data format, should be MM-DD-YYYY')

    @classmethod
    def validate_timecode_markers(self, timecode_markers):
        if len(timecode_markers) < 2 or len(timecode_markers) % 2 == 1:
            return False
        # loop through them and check if the timecodes are valid and in In-Out order.
        for i in range(0, len(timecode_markers), 2):
            in_code = timecode_markers[i]
            out_code = timecode_markers[i+1]

            # if either code is invalid or the combo isn't in the right order, return False
            if not self.validate_timecode(in_code) or \
                not self.validate_timecode(out_code) or \
                not self.are_timecodes_in_order(in_code, out_code):
                return False
        return True
    
    @classmethod
    def validate_timecode(self, timecode):
        pattern = re.compile(r'[0-9]{2}[;][0-5][0-9][;][0-5][0-9][;][0-2][0-9]')
        return pattern.match(timecode) and len(timecode) == 11

    @classmethod
    def are_timecodes_in_order(self, in_code, out_code):
        split_in_code = [int(time) for time in in_code.split(';')]
        split_out_code = [int(time) for time in out_code.split(';')]
        for i in range(4):
            in_time = split_in_code[i]
            out_time = split_out_code[i]
            if in_time > out_time:
                return False
            elif in_time < out_time:
                return True
        return False

    @classmethod
    def test_sample_input(self, file_path):
        # with open(self.TEST_FILE_PATH, 'r') as f:
            # lines = f.readlines()
            # for line in lines:
            #         parsed_line = line.rstrip().split("   ")
            #         parsed_line = self.process_text_line(line)

            #         print(parsed_line)
        return Marker.process_markers_file(file_path)


# Testing:
# sample_in = '00;00;21;29'
# sample_out = '00;00;22;03'
print(Marker.test_sample_input(Marker.TEST_FILE_PATH))
# print(Marker.test_sample_input())
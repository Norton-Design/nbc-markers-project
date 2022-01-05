import re
import datetime

class Marker:
    @classmethod
    def validate_markers_file(self, file):
        try:
            result = self.process_markers_file(file)
            if result:
                return result
            else:
                return {}
        except:
            return { 
                "error" : True,
                "message" : "File or timecodes doesn't conform to required format",
                    }

    @classmethod
    def process_markers_file(self, file):
        processed_lines = []
        line = file.read().decode("utf-8").rstrip()
        processed_lines.append(self.process_text_line(line))
        if len(processed_lines) == 1:
            return processed_lines[0]
        elif len(processed_lines) == 0:
            return { 'error': True, "message": "No processable lines" }
        else:
            # This is where we can expand later on the handle files that have multiple lines
            pass

    @classmethod
    def process_text_line(self, line):
        processed_data = {}
        section_list = line.rstrip().split("   ")
        asset_title, asset_id, material_type, date, *markers = section_list
        if self.validate_asset_title(asset_title):
            processed_data['asset_title'] = asset_title
        else:
            processed_data['error'] = True
            processed_data['message'] = 'Asset title cannot be blank and must not exceed 100 characters'
            return processed_data
        
        if self.validate_asset_id(asset_id):
            processed_data['asset_id'] = asset_id
        else:
            processed_data['error'] = True
            processed_data['message'] = 'Asset ID must be 4 uppercase alpha characters followed by 9 digits'
            return processed_data

        if self.validate_material_type(material_type):
            processed_data['material_type'] = material_type
        else:
            processed_data['error'] = True
            processed_data['message'] = 'Asset material type must be "news", "movie", "episode", or "sports"'
            return processed_data
        
        if self.validate_date(date):
            processed_data['date'] = date
        else:
            processed_data['error'] = True
            processed_data['message'] = "Date doesn't match the MM-DD-YYYY format"
            return processed_data

        if self.validate_timecode_markers(markers):
            processed_data['markers'] = self.process_timecode_markers(markers)
        else:
            processed_data['error'] = True
            processed_data['message'] = 'File contains an odd number of timecodes or an Out-code occurs before an In-code'
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
        try:
            datetime.datetime.strptime(date, '%m-%d-%Y')
        except ValueError:
            raise ValueError('Incorrect data format, should be MM-DD-YYYY')

    @classmethod
    def validate_timecode_markers(self, timecode_markers):
        if len(timecode_markers) < 2 or len(timecode_markers) % 2 == 1:
            return False
        for i in range(0, len(timecode_markers), 2):
            in_code = timecode_markers[i]
            out_code = timecode_markers[i+1]
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
        return Marker.process_markers_file(file_path)

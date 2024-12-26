PLACEHOLDER1 = '[name]'
INPUT_CONTENTS_PATH = "D24 - Mail-merger-project/Input/"
OUTPUT_CONTENTS_PATH = "D24 - Mail-merger-project/Output/"

with open(INPUT_CONTENTS_PATH + 'Names/invited_names.txt') as names:
    name_list = names.readlines()

with open(INPUT_CONTENTS_PATH + 'Letters/starting_letter.txt') as input_letter_file:
    content = input_letter_file.read()
    for name in name_list:
        curr_name = name.strip()
        changed_content = content.replace(PLACEHOLDER1, curr_name)
        with open(OUTPUT_CONTENTS_PATH + f'ReadyToSend/letter_to_{curr_name}.txt', 'w') as output_file:
            output_file.write(changed_content)

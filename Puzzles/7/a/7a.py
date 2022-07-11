from operator import itemgetter

steps = {}
executed_steps = []

def create_step_for_letter_if_needed(letter):
    if letter not in steps:
        step = {
            "letter": letter,
            "dependencies": []
        }
        steps[letter] = step

def step_for_letter(letter):
    step = steps[letter]
    return step

def step_is_ready(step):
    dependencies = step["dependencies"]
    step_is_ready = (len(dependencies) == 0)
    return step_is_ready

def ready_steps():
    ready_steps = []

    for step in steps.values():
        is_ready = step_is_ready(step)
        if is_ready:
            ready_steps.append(step)
    
    return ready_steps

def first_ready_step():
    sorted_steps = sorted(ready_steps(), key=itemgetter('letter'))
    first_step = sorted_steps[0]
    return first_step

def execute_step(step):
    executed_steps.append(step)
    letter = step["letter"]
    del steps[letter]
    delete_step_letter_from_dependencies(letter)

def delete_step_letter_from_dependencies(letter):
    for step in steps.values():
        dependencies = step["dependencies"]
        if letter in dependencies:
            dependencies.remove(letter)

def executed_letter_string():
    string = ""

    for step in executed_steps:
        letter = step["letter"]
        string = string + letter
    
    return string

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    lines = input_file.readlines()

    for line in lines:
        subject_step_letter = line[36]
        dependency_step_letter = line[5]

        create_step_for_letter_if_needed(subject_step_letter)
        create_step_for_letter_if_needed(dependency_step_letter)

        step = step_for_letter(subject_step_letter)
        dependencies = step["dependencies"]
        dependencies.append(dependency_step_letter)
        step["dependencies"] = dependencies
        steps[subject_step_letter] = step

    while (len(ready_steps()) > 0):
        first_step = first_ready_step()
        execute_step(first_step)

    print(executed_letter_string())

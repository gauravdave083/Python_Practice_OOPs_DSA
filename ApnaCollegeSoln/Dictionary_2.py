# List of subjects
subjects = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]

# Remove duplicate subjects and find the number of unique subjects
unique_subjects = set(subjects)
number_of_classrooms = len(unique_subjects)

# Print the result
print("Number of classrooms needed:", number_of_classrooms)
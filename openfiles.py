import unicodecsv

enrollments_filename = 'data/enrollments.csv'

## Longer version of code (replaced with shorter, equivalent version below)

# enrollments = []
# f = open(enrollments_filename, 'rb')
# reader = unicodecsv.DictReader(f)
# for row in reader:
#     enrollments.append(row)
# f.close()

with open(enrollments_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)
    
### Write code similar to the above to load the engagement
### and submission data. The data is stored in files with
### the given filenames. Then print the first row of each
### table to make sure that your code works. You can use the
### "Test Run" button to see the output of your code.

engagement_filename = 'data/daily_engagement.csv'
submissions_filename = 'data/project_submissions.csv'
    
daily_engagement = []

file_d = open(engagement_filename, "rb")

reader = unicodecsv.DictReader(file_d)

for row in reader:
    
    daily_engagement. append(row)
    
file_d.close()

print(daily_engagement[0])
    
project_submissions = []

file_p = open(submissions_filename,"rb")

reader = unicodecsv.DictReader(file_p)

for row in reader:
    
    project_submissions.append(row)
    
file_p.close()

print(project_submissions[0])
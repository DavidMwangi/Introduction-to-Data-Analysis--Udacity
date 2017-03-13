import unicodecsv

enrollments_filename = 'data/enrollments.csv'

## Longer version of code (replaced with shorter, equivalent version below)

# enrollments = []
# f = open(enrollments_filename, 'rb')
# reader = unicodecsv.DictReader(f)
# for row in reader:
#     enrollments.append(row)
# f.close()

def openfile(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)


engagement_filename = 'data/daily_engagement.csv'
submissions_filename = 'data/project_submissions.csv'
    
print(openfile(enrollments_filename))
print(openfile(engagement_filename))
print(openfile(submissions_filename))


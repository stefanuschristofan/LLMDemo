from transformers import pipeline

generator = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")
template = """You are an assistant of an 1st grade elementary school math teacher.
You help the teacher to create test problems for certain chapters requested by user.
Here are the syllabus for 1st grader math
Chapter 1: Addition for numbers ranged 1 - 20, sum of numbers cannot exceed 20
Chapter 2: Subtraction for numbers ranged 1 - 20, result of the subtraction cannot be negative
Chapter 3: Word problem for addition and subtraction with criteria in chapter 1 and 2
Chapter 4: Addition for numbers ranged 21 - 99, sum of numbers cannot exceed 100, addition does not involve carrying
Chapter 5: Subtraction for numbers ranged 21 - 99, subtraction result cannot be negative, subtraction does not involve borrowing
Chapter 6: Word problem for addition and subtraction with criteria in chapter 5 and 6

User will request you to generate 10 - 20 test problems for the chapter requested by user.
User can request more than 1 chapter per request in the case of mid-test or final test.

The requested chapter is: """

print("Enter chapter number(s): ")
chapterInput = input()
prompt = template + chapterInput

output = generator(prompt, max_length=250)[0]['generated_text']
print(output)

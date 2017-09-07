# -*- coding: utf-8 -*-
from Questioner.models import *
from uuid import uuid4
import random


questions_ans = [
	{ "question" :"What is your greatest strength?",
"answer": "This is one of the questions that employers almost always ask. When you are asked about your greatest strengths, it's important to discuss the attributes that will qualify you for the specific job and set you apart from the other candidates."
},
{ "question": "What is your greatest weakness?",
"answer": "Another typical question interviewers will ask is about your weaknesses. Do your best to frame your answers around positive aspects of your skills and abilities as an employee."},

{"question": "Tell me about yourself.",
"answer": "Here’s how to answer questions about you without giving out too much - or too little - personal information. Start by sharing some of your personal interests which don't relate directly to work."},

{"question": "Why should we hire you?",
"answer": "Are you the best candidate for the job? Be prepared to say why.  Make your response a concise sales pitch that explains what you have to offer the employer, and why you should get the job."},


{"question": "What are your salary expectations?",
"answer": "What are you looking for in terms of salary? It seems like a simple question, but your answer can knock you out of content for the job if you overprice yourself. Here's the best way to answer questions about salary."},

{"question": "Why are you leaving or have left your job?",
"answer": "When asked about why you are moving on, stick with the facts, be direct and focus your interview answer on the future, especially if your leaving wasn't under the best of circumstances."},

{"question": "Why do you want this job?",
"answer": "This question gives you an opportunity to show the interviewer what you know about the job and the company. Be specific about what makes you a good fit for this role, and mention aspects of the company and position that appeal to you."},

{"question": "How do you handle stress and pressure?",
"answer": "What do you do when things don’t go smoothly at work? The best way to respond to this question is to give an example of how you have handled stress in a previous job."},

{"question": "Describe a difficult work situation / project and how you overcame it.",
"answer": "The interviewer wants to know what you do when you face a difficult decision. As with the question about stress, be prepared to share an example of what you did in a tough situation."},


{"question": "What are your goals for the future?",
"answer": "This question is designed to find out if you’re going to stick around or move on as soon as you find a better opportunity. Keep your answer focused on the job and the company you’re interviewing with."}]

Question.objects.all().delete()
Answer.objects.all().delete()
Tenant.objects.all().delete()
User.objects.all().delete()


user_name = ["Nikhil Rane", "Vaibhav Muley", "Divyanjay Singh", "Abhishek Singh", "Nishant Pardamwar", "Rahul Patil", "Mohit Patil", "Ashutosh Narkhede"]

for i in user_name:
	user = User.objects.create(name=i)

users = [i for i in User.objects.all()]

for i in questions_ans:
	question = Question.objects.create(title=i['question'], user=user)
	for j in range(random.randint(1,5)):
		user = random.choice(users)	
		Answer.objects.create(body=i['answer'], user=user, question=question)
	print i

for i in user_name:
	tenant = Tenant.objects.create(name=i, api_key=str(uuid4()))
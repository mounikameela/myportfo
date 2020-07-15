from flask import Flask,render_template,request,redirect
import csv


app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html') 


# @app.route('/blog')
# def blog():
#    return 'Thes are my thoughts my blog!'

@app.route('/<string:page_name>')
def navigate_to_page(page_name):
 	return render_template(page_name) 

# @app.route('/components.html')
# def navigate_component_page():
# 	return render_template('components.html') 


# @app.route('/contact.html')
# def navigate_contact_page():
# 	return render_template('contact.html') 

# @app.route('/services.html')
# def navigate_services_page():
# 	return render_template('services.html')


def write_to_database_(data):
	with open('database.txt', mode= 'a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		database.write(f'\n {email} , {subject} ,{message} ')

def write_to_csv(data):
	with open('database.csv',newline='', mode= 'a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',')

		csv_writer.writerow([email,subject,message])
        

       





@app.route('/submit_form' , methods = ['POST','GET'])
def submit_form():
   if request.method == 'POST':

      data = request.form.to_dict()
      write_to_csv(data)
      return redirect('Thankyou.html')








from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():

   if request.method == "POST":
      name = request.form.get("name")
      email = request.form.get("email")
      
      with open("data.txt", "a") as file:
         data = f"{name}, {email}\n"
         file.write(data)
      return render_template("show_values.html", name=("Entered Name: " + name), email=("Entered Email: " + email))

   return render_template("index.html", current_time=("Date: " + time.asctime()))

@app.route('/style.css')
def get_css():
   return render_template("style.css")


@app.route('/show-values')
def show_data():
   names = []
   emails = []
   with open("data.txt", "r") as file:
      data = file.readlines()
      
      for line in data:
         line = line.removesuffix("\n")
         line = line.split(", ")
         print(line)
         names.append(line[0])
         emails.append(line[1])

   return render_template("show_values.html", name="Stored Names: "+ str(names), email="Stored Emails: " + str(emails))


if __name__ == '__main__':
   app.run()
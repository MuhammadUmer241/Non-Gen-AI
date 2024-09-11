import pandas as pd
from flask import Flask, render_template, url_for, request, jsonify


from utlis import open_pickle  # Assuming this opens a pickled model
from src.pipeline.predict_pipeline import predict_by_post  # Assuming this makes predictions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html", css_url=url_for('static', filename='style.css'))
    else:
        column_names = ["age", "job", "marital", "education", "default", "Some Loan",
                        "month", "poutcome", "contact",
                        "cons_conf_idx", "euribor3m", "nr_employed",
                        "previous_bins", "duration", "cons_price_idx"]


        data = {column: [request.form.get(column)] for column in column_names}
        ddf = pd.DataFrame(data)
        # Call the prediction function
        obj = predict_by_post()
        result = obj.predict(ddf)
        if result==0:
            result="NO"
        else:
            result = "Yes"
        return render_template("home.html",
                               css_url=url_for('static', filename='style.css'), results= result)
if __name__ == "__main__":
    app.run(debug=True)
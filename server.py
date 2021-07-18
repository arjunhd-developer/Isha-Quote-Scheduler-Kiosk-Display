from quote_scraper import QuoteScraper
from flask import Flask, render_template
from data_handling import DataHandler

app = Flask(__name__)


@app.route('/')
def home():
    quote = QuoteScraper()
    quote.get_quote()
    data_handler = DataHandler()
    data_handler.structure_data()
    data_handler.search_day()
    date_today = data_handler.today
    print(data_handler.master_data_set)
    return render_template(
        "home.html",
        quote_date=quote.quote_date.text,
        img_src=quote.quote_pic['src'],
        quote_text=quote.quote_text.div.text.strip(),
        master_data_set=data_handler.master_data_set,
        today=date_today
    )


if __name__ == "__main__":
    app.run(debug=True)


from newspaper import Article

def extract_text_from_url(url):
    try:

        article = Article(url)
        article.download()
        article.parse()
        result = {"title" : article.title,"text" : article.text}
        return result

    except Exception as e:
        return {"error" :str(e)}


if __name__ == "__main__":
    result = extract_text_from_url("https://en.wikipedia.org/wiki/Machine_learning")
    print(result)
from django.shortcuts import render
import requests
import json





URL = "https://jsonplaceholder.typicode.com/posts/1"

def get_request(url=None) -> dict:
    try:            
        response = requests.get(url=url)
        response.raise_for_status() # verifica se a resposta tem status de erro
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error when making the request {e}")
        return {}



def extract_body_from_response(response=None) -> str:
    return response.get("body", "Invalid Key!!")



def writer_json(body):
    try:
        with open('assets/static/data.json', "w") as json_file:
            json.dump(body, json_file)
    except FileNotFoundError as e:
        print(f"Error directory not found {e}")



def home_view(request):
    post = get_request(URL)
    post_body = extract_body_from_response(post)
    context = {
        'body': post_body,
    }

    return render(request, 'templates.html', context)



def main():
    post = get_request(URL)
    post_body = extract_body_from_response(post)

    data = {
        "body": post_body,
    }

    writer_json(data)



if __name__ == "__main__":
    main()
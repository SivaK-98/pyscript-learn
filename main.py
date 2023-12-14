from pyscript import document
def login():
  username = document.querySelector("#username")
  output_div = document.querySelector("#output")
  output_div.innerText = username
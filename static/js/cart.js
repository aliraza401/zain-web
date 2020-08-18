var updateBtns = document.getElementsByClassName("update-cart");

for (i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log(productId);
    console.log(action);

    if (user == "AnonymousUser") {
      alert("sorry", "you need to login");
    } else {
      UpdateUserOrder(productId, action);
      console.log("user in");
    }
  });
}

function UpdateUserOrder(productId, action) {
  // URL you want to send data
//   console.log(csrftoken)
  var url = "/update/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      productId: productId,
      action: action,
    }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("data:", data);
      location.reload();
    });
}

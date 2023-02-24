document.getElementById("my-form").addEventListener("submit", function (e) {
  e.preventDefault();
  const data = new FormData(e.target);

  const value = Object.fromEntries(data.entries());

  console.log({ value });

  const response = fetch("http://localhost:5000/submit-data", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": true,
    },
    body: JSON.stringify(value),
  }).then((resp) => {
    console.log(resp);

    chrome.tabs.create({
      url: `http://localhost:5000/test?email=${value.email}`,
    });
  });
});

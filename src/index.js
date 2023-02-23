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
      "Access-Control-Allow-Origin":true
    },
    body: JSON.stringify(value),
  })
    .then((resp) => {
      console.log(resp);

      navigator.mediaDevices
        .getUserMedia({ video: true, audio: true })
        .then(function (stream) {
          var video = document.querySelector("#video");
          video.srcObject = stream;
          video.play();

          const mediaRecorder = new MediaRecorder(stream);
          mediaRecorder.start();

          const audioChunks = [];
          mediaRecorder.addEventListener("dataavailable", (event) => {
            audioChunks.push(event.data);
          });

          mediaRecorder.addEventListener("stop", () => {
            const audioBlob = new Blob(audioChunks);
            const audioUrl = URL.createObjectURL(audioBlob);
            const audio = new Audio(audioUrl);
            audio.play();
          });
        });

      // Take pictures every 15 seconds
      setInterval(function () {
        const canvas = document.createElement("canvas");

        // Draw current video frame to canvas
        const context = canvas.getContext("2d");
        context.drawImage(video, 0, 0, canvas.width, canvas.height);

        // Convert canvas to data URL and send to server
        const dataURL = canvas.toDataURL();

        console.log(dataURL);

        fetch("http://localhost:5000/image", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": true,
          },
          body: JSON.stringify({
            image: dataURL,
            info: value.email
          
          }),
        })
          .then(function (response) {
            console.log("Image sent to server");
          })
          .catch(function (error) {
            console.log("Error sending image to server: ", error);
          });
        console.log("hello");
      }, 5000); // Interval in milliseconds

      return resp.json();
    })
    .then((data) => {
      console.log(data);
    })
    .catch((err) => {
      console.error(err);
    });
});

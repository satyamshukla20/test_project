window.addEventListener("load", async () => {
  const video = document.getElementById("video");

  const stream = await navigator.mediaDevices.getUserMedia({
    video: true,
    audio: true,
  });

  console.log(stream);

  video.srcObject = stream;
  video.play();

  console.log(video);

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

  // Take pictures every 15 seconds
  setInterval(function () {
    const canvas = document.createElement("canvas");

    // Draw current video frame to canvas
    const context = canvas.getContext("2d");
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Convert canvas to data URL and send to server
    const dataURL = canvas.toDataURL();

    console.log(dataURL);

    const params = new Proxy(new URLSearchParams(window.location.search), {
      get: (searchParams, prop) => searchParams.get(prop),
    });

    const email = params.email;

    fetch("http://localhost:5000/image", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": true,
      },
      body: JSON.stringify({
        image: dataURL,
        info: email,
      }),
    })
      .then(function (response) {
        console.log("Image sent to server");
      })
      .catch(function (error) {
        console.log("Error sending image to server: ", error);
      });
    console.log("hello");
  }, 5000); // captureing photo Interval in 5seconds
});

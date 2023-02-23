// chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
//   if (message && message.message === "Hello from content script!") {
//     sendResponse({ message: "Hello from service worker!" });

//     recording();
//   }
// });

// function recording() {
//   console.log("start recording");
//   navigator.mediaDevices
//     .getUserMedia({ video: true, audio: true })
//     .then(function (stream) {
//       var video = document.querySelector("#video");
//       video.srcObject = stream;
//       video.play();

//       const mediaRecorder = new MediaRecorder(stream);
//       mediaRecorder.start();

//       const audioChunks = [];
//       mediaRecorder.addEventListener("dataavailable", (event) => {
//         audioChunks.push(event.data);
//       });

//       mediaRecorder.addEventListener("stop", () => {
//         const audioBlob = new Blob(audioChunks);
//         const audioUrl = URL.createObjectURL(audioBlob);
//         const audio = new Audio(audioUrl);
//         audio.play();
//       });
//     });
// }

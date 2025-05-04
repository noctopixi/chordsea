const downloadLink = document.querySelector("#download");

const createTextFile = () => {
  console.log("you clicked")
  // Get the generated chord tabs
  const chordsText = document.querySelector("code").textContent;
  console.log(`Export text:${chordsText}`);

  // Store the tabs in a plaintext blob
  const blob = new Blob([chordsText], { type: "text/plain" });

  // Create URL for the blob so it can be downloaded
  const url = URL.createObjectURL(blob);
  downloadLink.href = url;

  // Revoke URL to free browser memory
  setTimeout(() => {
    URL.revokeObjectURL(url);
  }, 1000);
};

downloadLink.addEventListener("click", createTextFile);
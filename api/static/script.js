
function startProgress() {
    var progressBar = document.getElementById('progress-bar');
    var progress = 0;
    var interval = setInterval(function () {
        if (progress >= 100) {
            clearInterval(interval);
        } else {
            progress += 2;
            progressBar.style.width = progress + '%';
        }
    }, 600); // Adjust the interval and increment values as needed
}

// Function to be called when the form is submitted
function submitForm() {
    // Show the progress bar
    document.getElementById('progress-container').style.display = 'block';

    // Start the progress animation
    startProgress();
}

// Example: You can add an event listener to call submitForm when the form is submitted
document.getElementById('upload-form').addEventListener('submit', submitForm);

function handleFileSelect(fileIndex) {
    var fileInput = document.getElementById('fileInput' + fileIndex);
    var uploadSuccessMessage = document.getElementById('uploadSuccessMessage' + fileIndex);

    if (fileInput.files.length > 0) {
        uploadSuccessMessage.textContent = 'UPLOAD SUCCESSFUL';
        uploadSuccessMessage.style.display = 'block';
    } else {
        uploadSuccessMessage.style.display = 'none';
    }
}
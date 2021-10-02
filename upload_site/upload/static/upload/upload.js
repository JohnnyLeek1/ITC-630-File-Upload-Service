function uploadFile() {
    const fileInput = document.getElementById('file-upload');
    const uploadArea = document.getElementById('upload-area');
    const uploadingText = document.getElementById('uploading-text');

    const fileInputChange = e => {
        var files = e.target.files || e.dataTransfer.files;
    
        let toUpload = undefined;
        // Process all File objects
        for (var i = 0, f; f = files[i]; i++) {
            uploadArea.classList.add('hidden');

            uploadingText.innerHTML = `Uploading ${f.name}...`;
            uploadingText.classList.remove('hidden');

            toUpload = f;
        }

        if(toUpload !== undefined) {
            document.getElementById('upload-form').submit();
        }
    }


    fileInput.addEventListener('change', fileInputChange, false);

}
uploadFile();
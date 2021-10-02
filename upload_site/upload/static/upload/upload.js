function uploadFile() {

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const fileInput = document.getElementById('file-upload');
    const uploadArea = document.getElementById('upload-area');
    const uploadingText = document.getElementById('uploading-text');
    const cloudStorageInfo = document.getElementById('cloud-info');

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
            // let formData = new FormData();
            // formData.append('files[]', f);

            // fetch('/api/upload/', {
            //     method: 'POST',
            //     body: formData,
            //     headers: { 'X-CSRFToken': getCookie('csrftoken') }
            // }).then(response => response.json())
            // .then(data => console.log(data));
            document.getElementById('upload-form').submit();
        }
    }


    fileInput.addEventListener('change', fileInputChange, false);

}
uploadFile();
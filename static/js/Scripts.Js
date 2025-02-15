function copyToClipboard(elementId, button) {
    const text = document.getElementById(elementId).textContent;
    navigator.clipboard
        .writeText(text)
        .then(() => {
            button.textContent = "Copied";
            setTimeout(() => {
                button.textContent = "Copy";
            }, 2000);
        })
        .catch((err) => {
            console.error("Failed to copy text: ", err);
        });
}

function toggleVisibility(elementId) {
    const element = document.getElementById(elementId);
    if (element.style.display === "none") {
        element.style.display = "block";
    } else {
        element.style.display = "none";
    }
}

// Handle multiple file uploads
function handleFileUploads(event) {
    const files = event.target.files;
    Array.from(files).forEach((file) => {
        const formData = new FormData();
        formData.append("screenshot", file);

        // Send the screenshot to the server to generate a thumbnail
        fetch("/generate_thumbnail", {
            method: "POST",
            body: formData,
        })
            .then((response) => response.blob())
            .then((blob) => {
                const imageUrl = URL.createObjectURL(blob);
                addScreenshotCard(file, imageUrl); // Pass the original file name to the addScreenshotCard function
            })
            .catch((error) => alert("Error generating thumbnail: " + error));
    });
}

function addArchitectureUploader() {
    const container = document.getElementById("architecture-container");
    const uploader = document.createElement("div");
    uploader.classList.add("card");
    uploader.setAttribute("data-file-name", "");
    uploader.innerHTML = `
<div class="card-left">
    <div class="image-preview" style="display: none;">
        <img src="" alt="Uploaded Architecture Diagram" onclick="showImagePreview(this)" />
    </div>
    <button class="regenerate-button" onclick="regenerateImage('architecture Diagram.png', this)">🔄</button>
    <button class="download-button" onclick="downloadImage('architecture Diagram.png')">⬇️</button>
    <div class="upload-button">
        <input type="file" name="architecture_image" accept="image/*" onchange="handleFileUploadArchitecture(event)">
    </div>
</div>
<div class="card-right">
    <textarea name="architecture_desc" rows="3" placeholder="Describe the architecture diagram"></textarea>
</div>
`;
    container.appendChild(uploader);
}

// Add a new screenshot card dynamically for each file uploaded
function addScreenshotCard(file, imageUrl) {
    const container = document.getElementById("screenshots-container");
    const card = document.createElement("div");
    card.classList.add("card");
    card.setAttribute("data-file-name", file.name); // Store the original file name in a data attribute
    card.innerHTML = `
                <div class="card-left">
                    <div class="image-preview">
                        <img src="${imageUrl}" alt="Uploaded Screenshot" onclick="showImagePreview(this)" />
                    </div>
                    <button class="regenerate-button" onclick="regenerateImage('${file.name}', this)">🔄</button>
                    <button class="download-button" onclick="downloadImage('${imageUrl}')">⬇️</button>
                </div>
                <div class="card-right">
                    <textarea name="screenshot_desc" rows="3" placeholder="Describe the screenshot"></textarea>
                </div>
            `;
    container.appendChild(card);
}

function regenerateImage(fileName, button) {
    fetch(`/regenerate_thumbnail?file=${fileName}`)
        .then((response) => response.blob())
        .then((blob) => {
            const newImageUrl = URL.createObjectURL(blob);
            button.previousElementSibling.querySelector("img").src = newImageUrl;
        })
        .catch((error) => alert("Error regenerating image: " + error));
}

function regenerateImageThumbnail(fileName, button) {
    fetch(`/regenerate_thumbnail_arch?file=${fileName}`)
        .then((response) => response.blob())
        .then((blob) => {
            const newImageUrl = URL.createObjectURL(blob);
            button.previousElementSibling.querySelector("img").src = newImageUrl;
        })
        .catch((error) => alert("Error regenerating image: " + error));
}

function downloadImage(imageUrl) {
    const a = document.createElement("a");
    a.href = imageUrl;
    a.download = "downloaded_image.png";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

// Handle file upload for architecture images
function handleFileUploadArchitecture(event) {
    const input = event.target;
    const file = input.files[0];
    const card = input.closest(".card");
    const previewContainer = card.querySelector(".image-preview");
    const formData = new FormData();
    formData.append("screenshot", file);

    // Store the original file name in the data attribute
    card.setAttribute("data-file-name", file.name);

    // Send the architecture image to the server to generate a thumbnail
    fetch("/generate_thumbnail_arch", {
        method: "POST",
        body: formData,
    })
        .then((response) => response.blob())
        .then((blob) => {
            const imageUrl = URL.createObjectURL(blob);
            previewContainer.querySelector("img").src = imageUrl;
            previewContainer.style.display = "block";
        })
        .catch((error) => alert("Error generating thumbnail: " + error));
}

// Enable submit button only if all required fields are filled
function enableSubmitButton() {
    const requiredFields = document.querySelectorAll(".required");
    const submitButton = document.getElementById("submit-button");
    let allFilled = true;
    requiredFields.forEach((field) => {
        if (!field.value.trim()) {
            allFilled = false;
        }
    });
    submitButton.disabled = !allFilled;
}

// Updated submitProject function
async function submitProject(event) {
    event.preventDefault();

    const formElement = document.getElementById("project-form");
    const formData = new FormData(formElement);

    try {
        // Add screenshot file names and descriptions to formData if the checkbox is checked
        if (document.getElementById("checkbox-overview").checked) {
            const screenshotCards = document.querySelectorAll("#screenshots-container .card");
            screenshotCards.forEach((card, index) => {
                const fileName = card.getAttribute("data-file-name"); // Get the stored original file name
                const descriptionTextarea = card.querySelector("textarea[name='screenshot_desc']");

                if (fileName) {
                    formData.append(`screenshot_file_${index + 1}`, fileName); // Original file name
                }
                if (descriptionTextarea) {
                    formData.append(`screenshot_desc_${index + 1}`, descriptionTextarea.value); // Description
                }
            });
        }

        // Add architecture file names and descriptions to formData if the checkbox is checked
        if (document.getElementById("checkbox-architecture").checked) {
            const architectureCards = document.querySelectorAll("#architecture-container .card");
            architectureCards.forEach((card, index) => {
                const fileName = card.getAttribute("data-file-name"); // Get the stored original file name
                const descriptionTextarea = card.querySelector("textarea[name='architecture_desc']");

                if (fileName) {
                    formData.append(`architecture_file_${index + 1}`, fileName); // Original file name
                }
                if (descriptionTextarea) {
                    formData.append(`architecture_desc_${index + 1}`, descriptionTextarea.value); // Description
                }
            });
        }

        // Submit the form data via fetch
        const response = await fetch("/submit-project", {
            method: "POST",
            body: formData,
        });

        const data = await response.json();

        if (response.ok) {
            // Populate generated output fields only if the checkbox is checked
            if (document.getElementById("checkbox-youtube-script").checked) {
                document.getElementById("youtube-script-output").textContent = data.result.youtube_script_prompt || "";
            }
            if (document.getElementById("checkbox-youtube-description").checked) {
                document.getElementById("youtube-description-output").textContent = data.result.youtube_description_prompt || "";
            }
            if (document.getElementById("checkbox-readme").checked) {
                document.getElementById("readme-output").textContent = data.result.readme_file_prompt || "";
            }
            if (document.getElementById("checkbox-overview").checked) {
                document.getElementById("overview-output").textContent = data.result.blog_1_prompt || "";
            }
            if (document.getElementById("checkbox-demo").checked) {
                document.getElementById("demo-output").textContent = data.result.blog_2_prompt || "";
            }
            if (document.getElementById("checkbox-architecture").checked) {
                document.getElementById("architecture-output").textContent = data.result.architecture_prompt || "";
            }
            if (document.getElementById("checkbox-demo-video").checked) {
                document.getElementById("demo-video-output").textContent = data.result.demo_video_prompt || "";
            }
        } else {
            alert(`Error: ${data.error}`);
        }
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred while submitting the project.");
    }
}

function showImagePreview(imgElement) {
    const modal = document.getElementById("image-modal");
    const modalImage = document.getElementById("modal-image");

    // Set the modal image source to the clicked image
    modalImage.src = imgElement.src;

    // Show the modal
    modal.style.display = "block";
}

function closeImagePreview(event) {
    const modal = document.getElementById("image-modal");

    // Close the modal only if the clicked area is outside the image or the close button
    if (event.target === modal || event.target.classList.contains("image-close-btn")) {
        modal.style.display = "none";
    }
}

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Project Submission</title>
        <link rel="stylesheet" href="/static/styles.css" />
        <script>
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
                document.getElementById("overview-output").textContent = data.result.overview_prompt || "";
            }
            if (document.getElementById("checkbox-demo").checked) {
                document.getElementById("demo-output").textContent = data.result.demo_prompt || "";
            }
            if (document.getElementById("checkbox-architecture").checked) {
                document.getElementById("architecture-output").textContent = data.result.architecture_prompt || "";
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
        </script>
    </head>
    <body oninput="enableSubmitButton()">
        <div class="left-container">
            <!-- Section 1: Project Details -->
            <div class="form-section">
                <div class="wrapper">
                    <div class="btn close-btn"></div>
                    <div class="btn min-btn"></div>
                    <div class="btn max-btn"></div>
                </div>
                <h2>Project Details</h2>
                <form id="project-form" method="POST" enctype="multipart/form-data">
                    <div class="proj-desc-section">
                        <div class="input-group">
                            <label for="project-details">Description</label>
                            <textarea id="project-details" name="project_details" class="required" rows="4" placeholder="Enter project description" style=""></textarea>
                        </div>
                    </div>
                    <div class="proj-links-section">
                        <div class="input-group">
                            <label for="youtube-link">YouTube Link</label>
                            <input type="url" id="youtube-link" name="youtube_link" placeholder="Enter YouTube link" />
                        </div>
                        <div class="input-group">
                            <label for="github-link">GitHub Link</label>
                            <input type="url" id="github-link" name="github_link" placeholder="Enter GitHub link" />
                        </div>
                        <div class="input-group">
                            <label for="blog-link">Blog Link</label>
                            <input type="url" id="blog-link" name="blog_link" placeholder="Enter Blog link" />
                        </div>
                    </div>
                </form>
            </div>

            <!-- Section 2: File Uploads -->
            <div class="form-section">
                <h2>File Uploads</h2>

                <!-- Screenshots Section -->
                <script>
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
                </script>
                <h3>Screenshots</h3>
                <div class="screenshots-container" id="screenshots-container">
                    <!-- Screenshot Cards -->
                    <div class="upload-button">
                        <input type="file" name="screenshots" accept="image/*" multiple onchange="handleFileUploads(event)" />
                    </div>
                </div>

                <!-- Architecture Diagram Section -->
                <script>
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
                </script>
                <h3>Architecture Diagram</h3>
                <div class="architecture-container" id="architecture-container">
                    <div class="card" data-file-name="">
                        <div class="card-left">
                            <div class="image-preview" style="display: none">
                                <img src="" alt="Uploaded Architecture Diagram" onclick="showImagePreview(this)" />
                            </div>
                            <button class="regenerate-button" onclick="regenerateImageThumbnail('', this)">🔄</button>
                            <button class="download-button" onclick="downloadImage('')">⬇️</button>
                            <div class="upload-button">
                                <input type="file" name="architecture_image" accept="image/*" onchange="handleFileUploadArchitecture(event)" />
                            </div>
                        </div>
                        <div class="card-right">
                            <textarea name="architecture_desc" rows="3" placeholder="Describe the architecture diagram"></textarea>
                        </div>
                    </div>
                    <button class="plus-icon" onclick="addArchitectureUploader()">+</button>
                </div>
            </div>

            <!-- Modal for Full-Screen Preview -->
            <div id="image-modal" class="image-modal" onclick="closeImagePreview(event)">
                <span class="image-close-btn" onclick="closeImagePreview(event)">&times;</span>
                <img class="modal-content" id="modal-image" />
            </div>
            <!-- Submit Button -->
            <div class="button-container">
                <button id="submit-button" onclick="submitProject(event)" disabled="">Submit Project</button>
            </div>
        </div>
        <div class="right-container">
            <!-- Section 3: Generated Outputs -->
            <div class="form-section">
            <h2>Generated Outputs</h2>
            <div class="output-group">
                <h3>YouTube Video Script</h3>
                <input type="checkbox" id="checkbox-youtube-script" />
                <label for="checkbox-youtube-script">YouTube Video Script</label>
                <button class="copy-btn" onclick="copyToClipboard('youtube-script-output', this)">Copy</button>
                <button class="toggle-btn" onclick="toggleVisibility('youtube-script-output')">Hide/Show</button>
                <div id="youtube-script-output" class="output-box"></div>
            </div>
            <div class="output-group"></div>
                <h3>YouTube Video Description</h3>
                <input type="checkbox" id="checkbox-youtube-description" />
                <label for="checkbox-youtube-description">YouTube Video Description</label>
                <button class="copy-btn" onclick="copyToClipboard('youtube-description-output', this)">Copy</button>
                <button class="toggle-btn" onclick="toggleVisibility('youtube-description-output')">Hide/Show</button>
                <div id="youtube-description-output" class="output-box"></div>
            </div>
            <div class="output-group">
                <h3>README File</h3>
                <input type="checkbox" id="checkbox-readme" />
                <label for="checkbox-readme">README File</label>
                <button class="copy-btn" onclick="copyToClipboard('readme-output', this)">Copy</button>
                <button class="toggle-btn" onclick="toggleVisibility('readme-output')">Hide/Show</button>
                <div id="readme-output" class="output-box"></div>
            </div>
            <div class="output-group">
                <h3>Overview</h3>
                <input type="checkbox" id="checkbox-overview" />
                <label for="checkbox-overview">Overview</label>
                <button class="copy-btn" onclick="copyToClipboard('overview-output', this)">Copy</button>
                <button class="toggle-btn" onclick="toggleVisibility('overview-output')">Hide/Show</button>
                <div id="overview-output" class="output-box"></div>
            </div>
            <div class="output-group">
                <h3>Demo</h3>
                <input type="checkbox" id="checkbox-demo" />
                <label for="checkbox-demo">Demo</label>
                <button class="copy-btn" onclick="copyToClipboard('demo-output', this)">Copy</button>
                <button class="toggle-btn" onclick="toggleVisibility('demo-output')">Hide/Show</button>
                <div id="demo-output" class="output-box"></div>
            </div>
            <div class="output-group">
                <h3>Architecture Details</h3>
                <input type="checkbox" id="checkbox-architecture" />
                <label for="checkbox-architecture">Architecture Details</label>
                <button class="copy-btn" onclick="copyToClipboard('architecture-output', this)">Copy</button>
                <button class="toggle-btn" onclick="toggleVisibility('architecture-output')">Hide/Show</button>
                <div id="architecture-output" class="output-box"></div>
            </div>
            </div>
        </div>

        <script>
            function toggleVisibility(elementId) {
            const element = document.getElementById(elementId);
            if (element.style.display === "none") {
                element.style.display = "block";
            } else {
                element.style.display = "none";
            }
            }
        </script>

        <script>
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
        </script>
        <script src="/static/js/script.js"></script>
    </body>
</html>

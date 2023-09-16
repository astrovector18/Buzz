// Get references to the modal and buttons
const mobileModal = document.getElementById("mobile-modal");
const openModalButton = document.getElementById("open-modal");
const closeModalButton = document.getElementById("close-modal");
const header = document.querySelector(".desk-top-nav");

// Function to open the mobile modal
function openMobileModal() {
    mobileModal.style.display = "flex";
}

// Function to close the mobile modal
function closeMobileModal() {
    mobileModal.style.display = "none";
}

// Toggle between header and modal based on scre 
    if (window.innerWidth <= 768) {
        // Show the mobile modal on smaller screens
        header.style.display = "none";
       //openMobileModal();
    } else {
        // Show the header on larger screens
        header.style.display = "flex";
        closeMobileModal();
    }


// Add click event listeners to open and close the mobile modal
openModalButton.addEventListener("click", openMobileModal);
closeModalButton.addEventListener("click", closeMobileModal);

// Initial check and listen for window resize

//window.addEventListener("resize", toggleHeaderOrModal);
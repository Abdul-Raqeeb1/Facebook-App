// For edit buttons (tumhara old code)
const editButtons = document.querySelectorAll('.edit-btn');
const cancelButtons = document.querySelectorAll('.cancel-btn');

// Edit click event
editButtons.forEach(btn => {
  btn.addEventListener('click', e => {
    e.preventDefault();
    const parent = btn.parentElement;
    const form = parent.querySelector('.form-details');
    btn.style.display = 'none';
    form.style.display = 'block';
  });
});

// Cancel click event
cancelButtons.forEach(cancel => {
  cancel.addEventListener('click', () => {
    const form = cancel.parentElement;
    const parent = form.parentElement;
    const editBtn = parent.querySelector('.edit-btn');
    form.style.display = 'none';
    editBtn.style.display = 'inline-block';
  });
});

// ✅ Profile image upload code
const uploadImage = document.getElementById("uploadImage");
const fileInput = document.getElementById("fileInput");

uploadImage.addEventListener("click", () => fileInput.click());

fileInput.addEventListener("change", (e) => {
  const file = e.target.files[0];
  if (file) {
    uploadImage.src = URL.createObjectURL(file);
  }
});

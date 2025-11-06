    const toggleButton = document.getElementById('toggleButton');
    const contentToToggle = document.getElementById('contentToToggle');

    toggleButton.addEventListener('click', () => {
        
        if (contentToToggle.style.display === 'flex') {
            contentToToggle.style.display = 'none'; 
        } else {
            contentToToggle.style.display = 'flex';
        }
    });



    const createPostToggle = document.getElementById('createPostToggle');
    const showPost = document.getElementById('showPost');
    const con = document.getElementsByClassName('createPost-option')

    createPostToggle.addEventListener('click', () => {
        
        if (showPost.style.display == con) {
            showPost.style.display = 'none'; 
        } 
        else{
            showPost.style.display = 'flex';
        }

    });

function closePannel(){
    document.getElementById('showPost').style.display = 'none'
}

// function commentBtn(){
    
//     // const Comment_btn = document.getElementById('comment-btn');
//     const comment_input = document.getElementById('comment-input-Toggle');
//     const comment_box = document.getElementById('comment-box-Toggle');

//     // Comment_btn.addEventListener('click', () => {
        
//         if (comment_input.style.display == 'flex' && comment_box.style.display == 'flex') {
//             comment_input.style.display = 'none'; 
//             comment_box.style.display = 'none';
//         } 
//         else{
//             comment_input.style.display = 'flex';
//             comment_box.style.display = 'flex'
//         }

//     // });

// }

// Sabhi comment buttons select karo
const commentButtons = document.querySelectorAll('.comment-btn');

commentButtons.forEach(button => {
    
  button.addEventListener('click', () => {

    // Button ke closest card ko find karo
    const card = button.closest('.card');

    // Card ke baad jo siblings hain unme se comment box aur input dhoondo
    const commentBox = card.nextElementSibling;
    const commentInput = commentBox.nextElementSibling;

    // Display toggle logic
    if (
      commentBox.style.display === 'flex' &&
      commentInput.style.display === 'flex'
    ) {
      commentBox.style.display = 'none';
      commentInput.style.display = 'none';
    } else {
      commentBox.style.display = 'flex';
      commentInput.style.display = 'flex';
    }
  });
});


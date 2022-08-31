const error_btn = document.getElementById("close-error");
const error_msg = document.getElementById("error-msg");

const notification_btn = document.getElementById("close-notification");
const notification_msg = document.getElementById("notification-msg");

error_btn.addEventListener("click",()=>{
    error_msg.innerHTML=""
})

notification_btn.addEventListener("click",()=>{
    notification_msg.innerHTML=""
})
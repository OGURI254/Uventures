
$(function(){
    const form  = $('#contact-form')

    $(form).submit(function(e) {
        e.preventDefault()
        const firstName = $('#firstn')
        const lastName = $('#lastn')
        const email = $('#email')
        const phone = $('#phone')
        const subject = $('#subject')
        const message = $('#message')

        Mail::RTCRtpSender()

    })
})
// firstn,lastn,email,phone,subject,message


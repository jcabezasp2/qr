window.addEventListener('load', init);

const createEvents = () => {
    document.addEventListener('click', function (event) {
        const x = event.clientX / window.innerWidth;
        const y = event.clientY / window.innerHeight;
        confetti({
            origin: { x, y }
        });
    });

    document.querySelector('#button-marco').addEventListener('click', function (event) {
        document.querySelector('#artists-main').classList.add('d-none');
        document.querySelector('#marco').classList.remove('d-none');
    });

    document.querySelector('#button-andrea').addEventListener('click', function (event) {
        document.querySelector('#artists-main').classList.add('d-none');
        document.querySelector('#andrea').classList.remove('d-none');
    });

    document.querySelector('#button-chelina').addEventListener('click', function (event) {
        document.querySelector('#artists-main').classList.add('d-none');
        document.querySelector('#chelina').classList.remove('d-none');
    });

    const buttons = document.querySelectorAll('.artists-return');

    buttons.forEach(button => {
        button.addEventListener('click', function (event) {
            try{
                document.querySelector('#marco').classList.add('d-none');
                document.querySelector('#andrea').classList.add('d-none');
                document.querySelector('#chelina').classList.add('d-none');
            }finally{
                document.querySelector('#artists-main').classList.remove('d-none');
            }
        });
    });
    
    document.querySelector('#button-buy').addEventListener('click', function (event) {
        document.querySelector('#tickets-main').classList.add('d-none');
        document.querySelector('#tickets-form').classList.remove('d-none');
    });

}



function init() {

    createEvents();
    confetti();
    
};
function abrirModal(texto) {
    Swal.fire({
        title: `${texto}`,
        showClass: {
            popup: `
                animate__animated
                animate__fadeInUp
                animate__faster
            `
        },
        hideClass: {
            popup: `
                animate__animated
                animate__fadeOutDown
                animate__faster
            `
        },
        showCloseButton: false,
        allowOutsideClick: false,
        showConfirmButton: true,
    });
}
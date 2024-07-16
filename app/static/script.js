document.getElementById('employeeForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const data = Object.fromEntries(formData.entries());
    console.log(data);
    const response = await fetch('/add_employee', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (response.ok) {
        alert('Employé ajouté avec succès !');
        document.getElementById('employeeForm').reset();
    } else {
        alert('Erreur lors de l\'ajout de l\'employé.');
    }
});

const addButton = document.getElementById('add-table-btn');
const tableContainer = document.getElementById('table-container');
let tableCount = 1; // Initial table count

addButton.addEventListener('click', () => {
    if (tableCount < 3) {
        // Create a new table
        const newTable = document.createElement('table');
        newTable.classList.add('dynamic-table');
        tableContainer.appendChild(newTable);

        // Adjust table sizes
        const tableWidth = 85 / (tableCount + 1); // Divide screen width equally
        const existingTables = document.querySelectorAll('.dynamic-table');
        existingTables.forEach((table) => {
            table.style.width = `${tableWidth}%`;
        });

        tableCount++;
    }
});

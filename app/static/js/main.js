
document.addEventListener("DOMContentLoaded", function () {
    const sortableHeaders = document.querySelectorAll('th.sortable');
    const discountFilter = document.getElementById("filter-discount");
    const couponFilter = document.getElementById("filter-coupon");
    const clearFiltersBtn = document.getElementById("clear-filters");

    let currentSortColumn = null;
    let sortDirection = 1;

    function updateProductCount() {
        const visibleRows = document.querySelectorAll("table tbody tr:not([style='display: none;'])").length;
        document.getElementById("product-count").textContent = "Productos disponibles: " + visibleRows;
    }

    function applyFilters() {
        const discountRange = discountFilter.value ? discountFilter.value.split("-").map(Number) : null;
        const couponRange = couponFilter.value ? couponFilter.value.split("-").map(Number) : null;

        document.querySelectorAll("table tbody tr").forEach(row => {
            const discount = parseFloat(row.children[4].dataset.value) || 0;
            const coupon = parseFloat(row.children[4].dataset.coupon) || 0;

            let showRow = true;

            if (discountRange) {
                showRow = showRow && (discount >= discountRange[0] && discount <= discountRange[1]);
            }

            if (couponRange) {
                showRow = showRow && (coupon >= couponRange[0] && coupon <= couponRange[1]);
            }

            row.style.display = showRow ? "" : "none";
        });

        updateProductCount();
        if (currentSortColumn !== null) {
            sortTable(currentSortColumn, sortDirection);
        }
    }

    function sortTable(columnIndex, direction) {
        const tbody = document.querySelector('table tbody');
        const rows = Array.from(tbody.rows);

        rows.sort((a, b) => {
            const aValue = parseFloat(a.cells[columnIndex].dataset.value) || 0;
            const bValue = parseFloat(b.cells[columnIndex].dataset.value) || 0;
            return (aValue - bValue) * direction;
        });

        rows.forEach(row => tbody.appendChild(row));
    }

    sortableHeaders.forEach((header, index) => {
        header.addEventListener('click', () => {
            const columnIndex = index + 1;

            if (currentSortColumn === columnIndex) {
                sortDirection *= -1;
            } else {
                currentSortColumn = columnIndex;
                sortDirection = 1;
            }

            sortableHeaders.forEach(h => {
                h.classList.remove('sorted-asc', 'sorted-desc');
            });

            header.classList.add(sortDirection === 1 ? 'sorted-asc' : 'sorted-desc');
            sortTable(columnIndex, sortDirection);
        });
    });

    discountFilter.addEventListener("change", applyFilters);
    couponFilter.addEventListener("change", applyFilters);

    clearFiltersBtn.addEventListener("click", () => {
        discountFilter.value = "";
        couponFilter.value = "";
        document.querySelectorAll("table tbody tr").forEach(row => row.style.display = "");
        sortableHeaders.forEach(h => h.classList.remove('sorted-asc', 'sorted-desc'));
        currentSortColumn = null;
        updateProductCount();
    });

    updateProductCount();
});
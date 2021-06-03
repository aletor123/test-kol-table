$(document).ready(function () {
    let kols_table = $('.kolsTable').dataTable({
        order: [[0, "desc"]],
        columnDefs: [
            {
                searchPanes: {
                    show: false
                },
                orderable: true,
                searchable: true,
                targets: [0, 1, 2, 3, 4]
            },
        ],
        columns: [
            {
                title: 'First name',
                data: 'first_name',
                targets: [0]
            },
            {
                title: 'Middle name',
                data: 'middle_name',
                targets: [1]
            },
            {
                title: 'Last name',
                data: 'last_name',
                targets: [2]
            },
            {
                title: 'Credential',
                data: 'credential',
                targets: [3]
            },
            {
                title: 'Specialty',
                data: 'specialty',
                targets: [4]
            },
        ],
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        select: true,
        dom: 'Plfrtip',
        ajax: KOLS_URL
    });
});
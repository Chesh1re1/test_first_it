django.jQuery(function($) {
    function loadCategories(typeId, selectedCategoryId) {
        if (!typeId) {
            $('#id_category').html('<option value="">---------</option>').prop('disabled', true);
            $('#id_subcategory').html('<option value="">---------</option>').prop('disabled', true);
            return;
        }

        $.ajax({
            url: '/dds_app/get_categories/',
            data: {type_id: typeId},
            success: function(data) {
                var options = '<option value="">---------</option>';
                $.each(data, function(index, category) {
                    var selected = category.id == selectedCategoryId ? 'selected' : '';
                    options += '<option value="' + category.id + '" ' + selected + '>' + category.name + '</option>';
                });
                $('#id_category').html(options).prop('disabled', false);

                if (selectedCategoryId) {
                    loadSubcategories(selectedCategoryId, $('#id_subcategory').val());
                }
            }
        });
    }

    function loadSubcategories(categoryId, selectedSubcategoryId) {
        if (!categoryId) {
            $('#id_subcategory').html('<option value="">---------</option>').prop('disabled', true);
            return;
        }

        $.ajax({
            url: '/dds_app/get_subcategories/',
            data: {category_id: categoryId},
            success: function(data) {
                var options = '<option value="">---------</option>';
                $.each(data, function(index, subcategory) {
                    var selected = subcategory.id == selectedSubcategoryId ? 'selected' : '';
                    options += '<option value="' + subcategory.id + '" ' + selected + '>' + subcategory.name + '</option>';
                });
                $('#id_subcategory').html(options).prop('disabled', false);
            }
        });
    }

    $('#id_type').change(function() {
        var typeId = $(this).val();
        var selectedCategoryId = $('#id_category').val();
        loadCategories(typeId, selectedCategoryId);
    });

    $('#id_category').change(function() {
        var categoryId = $(this).val();
        var selectedSubcategoryId = $('#id_subcategory').val();
        loadSubcategories(categoryId, selectedSubcategoryId);
    });

    var initialTypeId = $('#id_type').val();
    var initialCategoryId = $('#id_category').val();
    var initialSubcategoryId = $('#id_subcategory').val();

    if (initialTypeId) {
        loadCategories(initialTypeId, initialCategoryId);
    }

    if (initialCategoryId) {
        loadSubcategories(initialCategoryId, initialSubcategoryId);
    }
});
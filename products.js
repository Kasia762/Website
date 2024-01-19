function products(){
    var outputProducts = document.getElementById("output-products");
    // Create a new paragraph element
    var paragraph = document.createElement("h1");
    // Set the text content of the paragraph
    paragraph.textContent = "Featured Products";
    // Append the paragraph to the output container
    outputProducts.appendChild(paragraph);

    var productsData=[
        ["Satin Elegance Dress", "Dress", 99.99, "Sapphire Blue", "ProductsCategoriesImages/shoes.jpg", "online"],
        ["Glamour Evening Dress", "Dress", 129.99, "Emerald Green", "ProductsCategoriesImages/shoes3.jpg", "online"],
        ["Fitter Blue Dress", "Dress", 79.99, "Royal Blue", "ProductsCategoriesImages/dress.jpg", "online"],
        ["Elegant Blue Dress", "Dress", 109.99, "Navy Blue", "ProductsCategoriesImages/dress2.jpg", "online"],
        ["Elegant Floral Dress", "Dress", 89.99, "Dusty Rose", "ProductsCategoriesImages/dress3.jpg", "online"],
        ["Satin Handbag", "Handbag", 49.99, "Champagne Gold", "ProductsCategoriesImages/handbag2.jpg", "online"],
        ["Glamour Clutch", "Handbag", 39.99, "Silver Gray", "ProductsCategoriesImages/handbag2.jpg", "online"],
        ["Fitter Tote Bag", "Handbag", 59.99, "Burgundy", "ProductsCategoriesImages/handbag3.jpg", "online"],
        ["Elegant Blue Jacket", "Jacket", 79.99, "Cerulean Blue", "ProductsCategoriesImages/jacket1.jpg", "online"],
        ["Satin Midi Skirt", "Skirt", 69.99, "Mauve Pink", "ProductsCategoriesImages/skirt1.jpg", "online"],
        ["Glamour Sequin Top", "Shirt", 34.99, "Rose Gold", "ProductsCategoriesImages/shirt1.jpg", "online"],
        ["Fitter Striped Dress", "Dress", 59.99, "Black & White", "ProductsCategoriesImages/dress.jpg", "online"],
        ["Elegant Lace Dress", "Dress", 89.99, "Ivory White", "ProductsCategoriesImages/dress.jpg", "online"],
        ["Satin Elegance Dress", "Dress", 99.99, "Sapphire Blue", "ProductsCategoriesImages/shoes.jpg", "online"],
        ["Glamour Evening Dress", "Dress", 129.99, "Emerald Green", "ProductsCategoriesImages/shoes3.jpg", "online"],
        ["Fitter Blue Dress", "Dress", 79.99, "Royal Blue", "ProductsCategoriesImages/dress.jpg", "online"],
        ["Elegant Blue Dress", "Dress", 109.99, "Navy Blue", "ProductsCategoriesImages/dress2.jpg", "online"],
        ["Elegant Floral Dress", "Dress", 89.99, "Dusty Rose", "ProductsCategoriesImages/dress3.jpg", "online"],
        ["Satin Handbag", "Handbag", 49.99, "Champagne Gold", "ProductsCategoriesImages/handbag2.jpg", "online"],
        ["Glamour Clutch", "Handbag", 39.99, "Silver Gray", "ProductsCategoriesImages/handbag2.jpg", "online"],
        ["Fitter Tote Bag", "Handbag", 59.99, "Burgundy", "ProductsCategoriesImages/handbag3.jpg", "online"],
        ["Elegant Blue Jacket", "Jacket", 79.99, "Cerulean Blue", "ProductsCategoriesImages/jacket1.jpg", "online"],
        ["Satin Midi Skirt", "Skirt", 69.99, "Mauve Pink", "ProductsCategoriesImages/skirt1.jpg", "online"],
    ];
    var nrItems = productsData.length
    var maxItemsRow = 5
    var maxRow = Math.floor(nrItems/maxItemsRow)
    // Loop through rows
    for (var i = 0; i < maxRow; i++) {
      // Create a new row element
      var row = document.createElement("div");
      row.classList.add("image-row");
      // Loop through columns
      for (var j = 0; j < maxItemsRow; j++) {
       // Create a new product container
       var productContainer = document.createElement("div");
       productContainer.classList.add("product-image-container");

       // Create a new image element
       var productImage = document.createElement("img");
       // Set the source of the image
       productImage.src = productsData[i * maxItemsRow + j][4];
       // Set alternative text for accessibility
       productImage.alt = "Product Image " + ((i * maxItemsRow) + j + 1);

       // Create a new text element
       var productName = document.createElement("p");
       // Set the text content of the text element
       productName.textContent = productsData[i * maxItemsRow + j][0];

       // Create a new text element
       var productPrice = document.createElement("p");
       // Set the text content of the text element
       productPrice.textContent = productsData[i * maxItemsRow + j][2] + "£";

       // Append the image and text to the product container
       productContainer.appendChild(productImage);
       productContainer.appendChild(productName);
       productContainer.appendChild(productPrice);

       // Append the product container to the row
       row.appendChild(productContainer);
   }
   // Append the row to the output container
   outputProducts.appendChild(row);
    }
  }
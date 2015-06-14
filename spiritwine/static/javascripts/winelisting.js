$(document).ready(function(){
            $("#wines-listing-items ul li:gt(5)").hide();
            var total_items=$("#wines-listing-items ul li").length;
            var items_per_page=6;
            var current_page_num=1;
            var total_page= Math.ceil(total_items/items_per_page);
            if (total_page == 0)
                total_page = 1;  
            var next=$("#wines-listing-pagebuttons .next");
            var prev=$("#wines-listing-pagebuttons .prev");
            $("#wines-listing-pagebuttons .total").text(total_page);
            $("#wines-listing-pagebuttons .current_pag").text(current_page_num);
             
            $("#wines-listing-pagebuttons .next").click(function(){
                if(current_page_num==total_page){
                        return false;
                    }
                    else{
                        $("#wines-listing-pagebuttons .current_page").text(++current_page_num);
                        $.each($('#wines-listing-items ul li'),function(index,item){
                            var start = items_per_page* (current_page_num-1);
                            var end = items_per_page * current_page_num;
                            if(index >= start && index < end){
                                $(this).show();
                            }else {
                                $(this).hide(); 
                            }
                        });
                    }
            });
            $("#wines-listing-pagebuttons .prev").click(function(){
                    if(current_page_num==1){
                        return false;
                    }else{
                        $("#wines-listing-pagebuttons .current_page").text(--current_page_num);
                        $.each($('#wines-listing-items ul li'),function(index,item){
                            var start = items_per_page* (current_page_num-1);
                            var end = items_per_page * current_page_num;
                            if(index >= start && index < end){
                                $(this).show();
                            }else {
                                $(this).hide(); 
                            }
                        });     
                    }
                     
                })
    })
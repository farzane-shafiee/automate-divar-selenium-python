
class FilterPageLocators:
    """
    All locators in page.
    """
    def __init__(self):
        self.locators = {
            "assert_page": '(//h2[@class="kt-post-card__title"])[1]',
            "assert_page_label": '//*[text()=" دیوار من "]',

            "search_box": '//form[@class="search-bar__input-form"]//input[@type="text"]',
            "assert_search_box": '//div[@class="kt-search-suggestion-row__title kt-text-truncate kt-body kt-body--sm"]',

            "vehicles_btn": '//*[contains(@href,"/s/tehran/vehicles")]',
            "auto_btn": '//*[contains(@href,"/s/tehran/auto") and text()="خودرو"]',
            "car_btn": '//*[contains(@href,"/s/tehran/") and text()="سواری و وانت"]',

            "color_btn": 'khesht-9',
            "color_checkbox": '//input[@type="checkbox" and @value="سفید"]/parent::div',
            "assert_delete_color_checkbox": '(//span[text()="حذف" and @class="kt-clear-section__title"])[1]',
            
            "price_btn": 'khesht-3',
            "assert_price_input": '//label[text()="حداکثر"]',
            "price_max_btn": '(//div[@id="khesht-2"]//button[@class="kt-select-field kt-select-field--small kt-select-field--normal"])[2]',
            "search_input": '//div[contains(@class,"kt-select-search")]//input[@placeholder="جستجو"]',
            "result_list_filter": '//ul[@class="kt-select-option-list kt-select-option-list--small"]',
            "assert_delete_price_box": '(//span[text()="حذف" and @class="kt-clear-section__title"])[2]',

            "immediate_btn": '//div[@class="filter-field--inline-d844c filter-field-c0991 filter-field__urgent"]',

            "filter_box": '//div[@class="browse-sidebar-ec193"]',
            "kilometers_btn": 'khesht-15',
            "assert_scroll": '//img[@alt="نشان نماد تجارت الکترونیکی"]',
            "assert_kilometers_input": '(//label[text()="تا"])[2]',
            "kilometers_max_btn": '(//div[@id="khesht-14"]//button[@class="kt-select-field kt-select-field--small kt-select-field--normal"])[1]',
            "assert_delete_kilometers_box": '(//span[text()="حذف" and @class="kt-clear-section__title"])[3]',

            "result_list_search": '//div[contains(@class,"browse-post-list-")]',
            "assert_select_one_item": '//button[contains(@class,"get-contact") and //span[text()="اطلاعات تماس"]]'
        }

    def __getitem__(self, index):
        return self.locators[index]

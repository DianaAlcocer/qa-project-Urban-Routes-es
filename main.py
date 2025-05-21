import data
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
    return str(code)

class UrbanRoutesPage:

    # Set_address
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Select_transport_mode
    mode_selector = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[1]/div[1]')
    flash_button = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[1]/div[1]/div[2]')
    personal_button = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[1]/div[1]/div[3]')

    # Select_transport_type
    taxi_status = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[1]/div[2]/div[3]')
    taxi_button = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[1]/div[2]/div[3]/img')

    # Select_taxi-tariff
    tariff_cards_selector = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]')
    comfort_status = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    comfort_button = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')

    # Set_transport
    book_taxi = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')

    # Set-user_phone_number
    button_add_phone_number = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')
    phone_number = (By.XPATH,"//input[@id='phone']")
    button_summit_phone = (By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')

    # Set-user_phone_code
    phone_code = (By.XPATH,'//*[@id="code"]')
    button_summit_code = (By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')

    # Set-user_payment
    button_add_payment = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]')
    button_add_creditcard = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    credit_card_number = (By.ID,'number')
    #credit_card_number_1 = (By.XPATH,'//*[@id="number"]')
    credit_card_code = (By.NAME, 'code')
    #credit_card_code_1 = (By.XPATH,'//*[@id="code"]')
    #credit_card_code_2 = (By.ID, 'code')
    #credit_card_code_3 = (By.CLASS_NAME, 'card-input')
    button_add_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    button_close_card_window = (By.XPATH,'(//button[@class="close-button section-close"])[3]')

    # Input_message_for_driver
    message_for_driver = (By.NAME,'comment')

    # Additional_items
    blanket_handkerchief_slider = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div')
    blanket_handkerchief_status = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input')
    ice_cream_add_button = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    ice_cream_counter = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')

    # Pedir_taxi
    confirm_taxi = (By.CLASS_NAME,'smart-button')
    #confirm_taxi_1 = (By.XPATH,'//*[@id="root"]/div/div[3]/div[4]/button')

    # Buscar_automóvil
    search_taxi = (By.XPATH,'//*[@id="root"]/div/div[5]')

    # Informacion_del_viaje


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def wait_for_load_set_route_input(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.from_field))

    def wait_for_load_transport_selection(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.mode_selector))

    def wait_for_load_tariff_cards(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.tariff_cards_selector))

    def wait_for_load_phone_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.button_add_phone_number))

    def wait_for_load_payment_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.button_add_payment))

    def wait_for_load_cvv_input(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.credit_card_code))

    def wait_for_load_close_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.button_close_card_window))

    def page_down_1(self):
        for _ in range(1):
            self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)

    def page_down_2(self):
        for _ in range(2):
            self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)

    def set_route(self,address_from,address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def select_transport_taxi(self):
        # Está inhabilitado el modo 'Óptimo' y 'Flash', las siguientes líneas se usarían en caso de que
        # no estuviera preseleccionado el tipo 'Taxi'.
        #self.driver.find_element(*self.personal_button).click()
        #self.driver.find_element(*self.taxi_button).click()

        # Por defecto está seleccionado el modo 'Flash' y tipo 'Taxi'.
        self.driver.find_element(*self.book_taxi).click()

    def transport_taxi_status(self):
        return self.driver.find_element(*self.taxi_status).get_attribute('class')

    def select_taxi_comfort(self):
        self.driver.find_element(*self.comfort_button).click()

    def taxi_comfort_status(self):
        return self.driver.find_element(*self.comfort_status).get_attribute('class')

    def input_phone_number(self,user_phone_number):
        self.driver.find_element(*self.phone_number).clear()
        self.driver.find_element(*self.phone_number).send_keys(user_phone_number)

    def input_phone_code(self,user_phone_code):
        self.driver.find_element(*self.phone_code).send_keys(user_phone_code)

    def set_user_phone_number(self,user_phone_number):
        self.driver.find_element(*self.button_add_phone_number).click()
        self.input_phone_number(user_phone_number)
        self.driver.find_element(*self.button_summit_phone).click()
        user_phone_code = retrieve_phone_code(self.driver)
        self.input_phone_code(user_phone_code)
        self.driver.find_element(*self.button_summit_code).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number).get_property('value')

    def input_credit_card_number(self,card_number):
        self.driver.find_element(*self.credit_card_number).click()
        self.driver.find_element(*self.credit_card_number).send_keys(card_number)

    def input_credit_card_code(self, card_code):
        self.wait_for_load_cvv_input()
        self.driver.find_element(*self.credit_card_code).click()
        self.driver.find_element(*self.credit_card_code).send_keys(card_code + Keys.TAB)

    def add_user_credit_card(self,card_number,card_code):
        self.driver.find_element(*self.button_add_payment).click()
        self.driver.find_element(*self.button_add_creditcard).click()
        self.input_credit_card_number(card_number)
        self.input_credit_card_code(card_code)
        self.driver.find_element(*self.button_add_card).click()
        self.wait_for_load_close_button()
        self.driver.find_element(*self.button_close_card_window).click()

    def get_credit_card_number(self):
        return self.driver.find_element(*self.credit_card_number).get_property('value')

    def get_credit_card_code(self):
        return self.driver.find_element(*self.credit_card_code).get_property('value')

    def input_message_for_driver(self,message):
        self.driver.find_element(*self.message_for_driver).send_keys(message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_for_driver).get_property('value')

    def order_blanket_handkerchief(self,blanket):
        if blanket:
            self.driver.find_element(*self.blanket_handkerchief_slider).click()

    def slider_blanket_status(self):
        return self.driver.find_element(*self.blanket_handkerchief_status)

    def order_ice_cream(self,ice_cream):
        for _ in range(ice_cream):
            self.driver.find_element(*self.ice_cream_add_button).click()

    def get_ice_cream_counter(self):
        counter = self.driver.find_element(*self.ice_cream_counter).text
        return int(counter)

    def button_book_a_taxi(self):
        return self.driver.find_element(*self.confirm_taxi)

    def click_button_book_a_taxi(self):
        self.button_book_a_taxi().click()

    def search_taxi_window(self):
        return self.driver.find_element(*self.search_taxi).get_attribute('class')

class TestUrbanRoutes:

    driver = None

#    @classmethod
#    def setup_class(cls):
#        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de
#        # confirmación del teléfono
#        from selenium.webdriver import DesiredCapabilities
#        capabilities = DesiredCapabilities.CHROME
#        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
#        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    @classmethod
    def setup_class(cls):
        # En el setup_class(cls) original, marca 'unexpected argument' para 'desired_capabilities'.
        # Lo que indica que este argumento ya no es compatible con las nuevas versiones de Selenium,
        # dicho argumento se sustituyo por el objeto 'Options'.
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_set_route_input()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_transport_taxi(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_transport_selection()
        routes_page.select_transport_taxi()
        taxi_status = routes_page.transport_taxi_status()
        assert 'active' in taxi_status

    def test_transport_taxi_comfort(self):
        self.test_transport_taxi()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_taxi_comfort()
        comfort_status = routes_page.taxi_comfort_status()
        assert 'active' in comfort_status

    def test_set_phone_number(self):
        self.test_transport_taxi_comfort()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_phone_button()
        routes_page.page_down_1()
        user_phone_number = data.phone_number
        routes_page.set_user_phone_number(user_phone_number)
        assert routes_page.get_phone_number() == user_phone_number

    def test_set_payment(self):
        self.test_transport_taxi_comfort()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_payment_button()
        routes_page.page_down_1()
        card_number = data.card_number
        card_code = data.card_code
        routes_page.add_user_credit_card(card_number,card_code)
        assert routes_page.get_credit_card_number() == card_number
        assert routes_page.get_credit_card_code() == card_code

    def test_message_for_driver(self):
        self.test_transport_taxi_comfort()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.page_down_1()
        message = data.message_for_driver
        routes_page.input_message_for_driver(message)
        assert routes_page.get_message_for_driver() == message

    def test_add_blanket_handkerchief(self):
        self.test_transport_taxi_comfort()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.page_down_1()
        initial_status = routes_page.slider_blanket_status().is_selected()
        blanket = data.blanket_handkerchief_order
        routes_page.order_blanket_handkerchief(blanket)
        final_status = routes_page.slider_blanket_status().is_selected()
        assert initial_status != final_status
        assert final_status == True

    def test_add_ice_cream(self):
        self.test_transport_taxi_comfort()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.page_down_2()
        ice_cream = data.ice_cream_order
        routes_page.order_ice_cream(ice_cream)
        assert routes_page.get_ice_cream_counter() == ice_cream

    def test_button_book_a_taxi(self):
        #Precondiciones
        self.test_transport_taxi_comfort()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_phone_button()
        routes_page.page_down_1()
        user_phone_number = data.phone_number
        routes_page.set_user_phone_number(user_phone_number)
        routes_page.wait_for_load_payment_button()
        routes_page.page_down_1()
        card_number = data.card_number
        card_code = data.card_code
        routes_page.add_user_credit_card(card_number, card_code)

        #Test
        button_book_a_taxi = routes_page.button_book_a_taxi()
        assert button_book_a_taxi.is_enabled() == True

#    def test_search_taxi_window(self):
#        #Precondiciones
#        self.test_button_book_a_taxi()
#        routes_page = UrbanRoutesPage(self.driver)
#
#        #Test
#        window_search_taxi = routes_page.search_taxi_window()
#        assert 'shown' in window_search_taxi

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

class TestBookATaxi:

    driver = None

    @classmethod
    def setup_class(cls):
        # En el setup_class(cls) original, marca 'unexpected argument' para 'desired_capabilities'.
        # Lo que indica que este argumento ya no es compatible con las nuevas versiones de Selenium,
        # dicho argumento se sustituyo por el objeto 'Options'.
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()

    def test_book_a_taxi(self):

        # Specifications: Tariff = Comfort, Add Blanket and Handkerchief, Add 2 ice cream

        # General

        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Set Route

        routes_page.wait_for_load_set_route_input()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

        # Set Transport Type

        routes_page.wait_for_load_transport_selection()
        routes_page.select_transport_taxi()
        taxi_status = routes_page.transport_taxi_status()
        assert 'active' in taxi_status

        routes_page.select_taxi_comfort()
        comfort_status = routes_page.taxi_comfort_status()
        assert 'active' in comfort_status

        # Scroll down the view

        routes_page.page_down_1()

        # Set Phone Number

        routes_page.wait_for_load_phone_button()
        user_phone_number = data.phone_number
        routes_page.set_user_phone_number(user_phone_number)
        assert routes_page.get_phone_number() == user_phone_number

        # Set Payment

        routes_page.wait_for_load_payment_button()
        card_number = data.card_number
        card_code = data.card_code
        routes_page.add_user_credit_card(card_number, card_code)
        assert routes_page.get_credit_card_number() == card_number
        assert routes_page.get_credit_card_code() == card_code

        # Set Message for driver

        message = data.message_for_driver
        routes_page.input_message_for_driver(message)
        assert routes_page.get_message_for_driver() == message

        # Scroll down the view

        routes_page.page_down_1()

        # Set Additional items: Blanket and handkerchief

        initial_status = routes_page.slider_blanket_status().is_selected()
        blanket = data.blanket_handkerchief_order
        routes_page.order_blanket_handkerchief(blanket)
        final_status = routes_page.slider_blanket_status().is_selected()
        assert initial_status != final_status
        assert final_status == True

        # Set Additional items: Ice cream

        ice_cream = data.ice_cream_order
        routes_page.order_ice_cream(ice_cream)
        assert routes_page.get_ice_cream_counter() == ice_cream

        # Confirm trip

        button_book_a_taxi = routes_page.button_book_a_taxi()
        assert button_book_a_taxi.is_enabled() == True
        routes_page.click_button_book_a_taxi()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
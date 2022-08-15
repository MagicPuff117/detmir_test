import requests
import json
import csv


def collect_data():

    cookies = {
        'ab2_90': 'ab2_90old90',
        'ab2_33': 'ab2_33new33',
        'ab2_50': '44',
        'ab3_75': 'ab3_75new20',
        'ab3_33': 'ab3_33old17',
        'ab3_20': 'ab3_20_10_1',
        'cc': '0',
        '_gaexp': 'GAX1.2.8MwGXf_UQwWf1g2n0sBLCw.19243.1',
        '_ym_uid': '166037581783949632',
        '_ym_d': '1660375817',
        '_gcl_au': '1.1.504149910.1660375817',
        '_ga': 'GA1.2.1008689479.1660375817',
        '_gid': 'GA1.2.799145228.1660375817',
        'tmr_lvid': '7d1e30bd37859380379fdda63d5a42f5',
        'tmr_lvidTS': '1660375817663',
        'advcake_track_id': '953968bf-e66e-55c0-c977-81f3efed15e9',
        'advcake_session_id': '05ce8517-4258-8a01-1232-07dcd2a07644',
        'auid': '5899842b-f50a-43b3-b8b3-1f8bdbdebd39',
        'geoCityDM': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C',
        'geoCityDMIso': 'RU-MOW',
        'geoCityDMCode': '7700000000000',
        'uid': 'X6NyEmL4o8ycIbnoEyrMAg==',
        '_ym_isad': '2',
        'JSESSIONID': 'b12b1660-1c9e-44de-9448-ff94b502db68',
        'detmir-cart': '36e4b31f-5b64-4c02-9615-d838f2fb9f9b',
        'srv_id': 'cubic-front03-prod',
        'adrdel': '1',
        'adrcid': 'Az9f4VAe7ArWIrl_DGigpNQ',
        '_ym_visorc': 'w',
        '_sp_ses.2b21': '*',
        'qrator_msid': '1660475356.071.iPRKWflKaalmT05c-fp284geo86j9tsld24ndsrqetoi6chnc',
        '_gat': '1',
        '_gat_test': '1',
        '_sp_id.2b21': '3d9b6f47-225c-45d4-9aee-c4cf540019ca.1660375817.5.1660476060.1660472626.14eac13b-3c10-4cd2-a16e-a61d1ee86e48',
        'mindboxDeviceUUID': '70d761f3-6c06-4341-ae61-dc5225e31274',
        'directCrm-session': '%7B%22deviceGuid%22%3A%2270d761f3-6c06-4341-ae61-dc5225e31274%22%7D',
        'tmr_reqNum': '177',
        'dm_s': 'L-b12b1660-1c9e-44de-9448-ff94b502db68|kH36e4b31f-5b64-4c02-9615-d838f2fb9f9b|Vj5899842b-f50a-43b3-b8b3-1f8bdbdebd39|gqcubic-front03-prod|qa96f62230-f394-41bb-b5f6-a308f104f2fb|RK1660476062037|-N1660476062025|11cc66ea69-4ead-45ff-a1f8-66e3fe7ed678#xP1fkhoFYiSWhBw5bJ_i6ZlFRfHClS0AqSDOV2jW914',
    }

    headers = {
        'authority': 'api.detmir.ru',
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9',
        'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'ab2_90=ab2_90old90; ab2_33=ab2_33new33; ab2_50=44; ab3_75=ab3_75new20; ab3_33=ab3_33old17; ab3_20=ab3_20_10_1; cc=0; _gaexp=GAX1.2.8MwGXf_UQwWf1g2n0sBLCw.19243.1; _ym_uid=166037581783949632; _ym_d=1660375817; _gcl_au=1.1.504149910.1660375817; _ga=GA1.2.1008689479.1660375817; _gid=GA1.2.799145228.1660375817; tmr_lvid=7d1e30bd37859380379fdda63d5a42f5; tmr_lvidTS=1660375817663; advcake_track_id=953968bf-e66e-55c0-c977-81f3efed15e9; advcake_session_id=05ce8517-4258-8a01-1232-07dcd2a07644; auid=5899842b-f50a-43b3-b8b3-1f8bdbdebd39; geoCityDM=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C; geoCityDMIso=RU-MOW; geoCityDMCode=7700000000000; uid=X6NyEmL4o8ycIbnoEyrMAg==; _ym_isad=2; JSESSIONID=b12b1660-1c9e-44de-9448-ff94b502db68; detmir-cart=36e4b31f-5b64-4c02-9615-d838f2fb9f9b; srv_id=cubic-front03-prod; adrdel=1; adrcid=Az9f4VAe7ArWIrl_DGigpNQ; _ym_visorc=w; _sp_ses.2b21=*; qrator_msid=1660475356.071.iPRKWflKaalmT05c-fp284geo86j9tsld24ndsrqetoi6chnc; _gat=1; _gat_test=1; _sp_id.2b21=3d9b6f47-225c-45d4-9aee-c4cf540019ca.1660375817.5.1660476060.1660472626.14eac13b-3c10-4cd2-a16e-a61d1ee86e48; mindboxDeviceUUID=70d761f3-6c06-4341-ae61-dc5225e31274; directCrm-session=%7B%22deviceGuid%22%3A%2270d761f3-6c06-4341-ae61-dc5225e31274%22%7D; tmr_reqNum=177; dm_s=L-b12b1660-1c9e-44de-9448-ff94b502db68|kH36e4b31f-5b64-4c02-9615-d838f2fb9f9b|Vj5899842b-f50a-43b3-b8b3-1f8bdbdebd39|gqcubic-front03-prod|qa96f62230-f394-41bb-b5f6-a308f104f2fb|RK1660476062037|-N1660476062025|11cc66ea69-4ead-45ff-a1f8-66e3fe7ed678#xP1fkhoFYiSWhBw5bJ_i6ZlFRfHClS0AqSDOV2jW914',
        'origin': 'https://www.detmir.ru',
        'referer': 'https://www.detmir.ru/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.1.828 (beta) Yowser/2.5 Safari/537.36',
        'x-requested-with': 'detmir-ui',
    }

    response = requests.get(
        'https://api.detmir.ru/v2/recommendation/products?filter=category.id:44733;placement:web_listing_popular;region.iso:RU-MOW&limit=30&offset=0',
        cookies=cookies, headers=headers).json()

    products= response.get('products')
    print(len(products))
    product_info = []

    for item in products:
        item_id = item.get('id')
        item_name = item.get('title')
        item_price_promo = item.get('price').get('price')
        try:
            item_price = item.get('old_price').get('price')
        except AttributeError:
            item_price = 'None'
        item_url = item.get('link').get('web_url')

        items_data = {
            'id': item_id,
            'Название': item_name,
            'Цена': item_price,
            'Цена_со_скидкой': item_price_promo,
            'Ссылка на товар': item_url
        }
        product_info.append(items_data)

        columns = [
            'id',
            'Название',
            'Цена',
            'Цена_со_скидкой',
            'Ссылка на товар']

        with open('products.csv', 'w')as f:
            wr = csv.DictWriter(f, fieldnames=columns)
            wr.writeheader()
            wr.writerows(product_info)


def main():
    collect_data()


if __name__ == '__main__':
    main()
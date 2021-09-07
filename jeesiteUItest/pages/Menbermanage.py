import time

from selenium.webdriver.common.by import By

from pages.Base_page import BasePage


class Menbermanage(BasePage):
    def AddMenber(self):
        # 切换到用户管理的iframe
        self.switch_frame(1)
        self.switch_frame('mainFrame')
        # 点击新增
        self.find(By.CSS_SELECTOR, '.fa-plus').click()
        # 切回原来的frame
        self.switch_beforframe()
        self.switch_beforframe()
        # 切换到新增用户frame
        self.switch_frame(2)
        # 点击打开归属机构查询
        self.finds(By.CSS_SELECTOR, '.fa-search')[0].click()
        # time.sleep(2)
        # 切换退出frame
        self.switch_beforframe()
        # 切换到第三个frame，机构选择页面
        self.switch_frame(3)
        # 点击选择济南公司
        self.wait_for_click((By.XPATH, '//*[@id="tree_2_span"]'))
        self.find(By.XPATH, '//*[@id="tree_2_span"]').click()
        # 点击选择企管部
        self.wait_for_click((By.ID, 'tree_3_span'))
        self.find(By.ID, 'tree_3_span').click()
        # 切换退出frame
        self.switch_beforframe()
        # 点击确定，选择归属机构
        self.find(By.CSS_SELECTOR, '.layui-layer-btn0').click()
        # 切换至新增用户的frame
        self.switch_frame(2)
        # 打开归属公司的查询框
        self.finds(By.CSS_SELECTOR, '.fa-search')[1].click()
        time.sleep(1)
        # 切换回原frame
        self.switch_beforframe()
        # 切换至归属公司选择框的frame
        self.switch_frame(3)
        # 点击济南公司
        self.find(By.ID, 'tree_2_span').click()
        # 返回原frame
        self.switch_beforframe()
        # 点击确定
        self.find(By.CSS_SELECTOR, '.layui-layer-btn0').click()
        # 点击登录账号输入框
        self.switch_frame(2)
        self.find(By.NAME, 'loginCode').click()
        # 输入登录账号
        self.find(By.ID,'loginCode').send_keys('huqingwei')
        # 点击用户昵称输入框
        self.find(By.ID, "userName").click()
        # 输入用户昵称
        self.find(By.ID, "userName").send_keys('嘟嘟D')
        # 勾选部门经理
        self.find(By.ID, 'jqg_roleGrid_dept').click()
        # 点击确定保存
        self.find(By.ID, 'btnSubmit').click()



    def get_menber(self,aimtitle):
        time.sleep(2)
        self.switch_beforframe()
        self.switch_frame(1)
        self.switch_frame('mainFrame')
        title = self.find(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[3]').text
        if title == aimtitle:
            return True
        else:
            return False

    def deletemenber(self,account):
        userid = []
        # 切换到目标iframe
        self.switch_frame(1)
        self.switch_frame('mainFrame')
        # 收集userid
        for i in range(2,22):
            id = self.find(By.CSS_SELECTOR, '.ui-jqgrid-btable>tbody>tr:nth-child('+str(i)+')').get_attribute('id')
            userid.append(id)
        # 循环判断userid是否在列表里，在的话点击删除
        for i in range(0,21):
            if account in userid[i]:
                self.find(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr['+str(i+2)+']/td[12]/a[3]/i').click()
                self.switch_beforframe()
                self.switch_beforframe()
                self.wait_for_click((By.CSS_SELECTOR, '.layui-layer-btn0'))
                self.find(By.CSS_SELECTOR, '.layui-layer-btn0').click()
                time.sleep(2)
                self.switch_frame(1)
                self.switch_frame('mainFrame')
                seccondid = self.find(By.CSS_SELECTOR, '.ui-jqgrid-btable>tbody>tr:nth-child(' + str(i + 2) + ')').get_attribute('id')
                checkid = userid[i+1]
                break
        if seccondid == checkid:
            return True
        else:
            return False

    def altermenberinfo(self, mobilenumber):
        # 切换至用户管理的iframe
        self.switch_frame(1)
        self.switch_frame('mainFrame')
        # 点击第一个数据行的修改按钮
        self.find(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[12]/a[1]/i').click()
        time.sleep(2)
        # 回退到原初的iframe
        self.switch_beforframe()
        self.switch_beforframe()
        # 进入到编辑用户iframe
        self.switch_frame(2)
        # 清空手机号码栏，并输入手机号码
        self.find(By.ID, 'mobile').clear()
        self.find(By.ID, 'mobile').send_keys(mobilenumber)
        # 点击保存按钮
        self.find(By.ID, 'btnSubmit').click()
        time.sleep(2)
        # 切换至用户管理iframe
        self.switch_beforframe()
        self.switch_frame(1)
        self.switch_frame('mainFrame')
        # 对比输入的手机号和界面显示的手机号
        newmobilenumber = self.find(By.CSS_SELECTOR, '.ui-jqgrid-btable>tbody>tr:nth-child(2)>td:nth-child(8)').get_attribute('innerText')
        if mobilenumber == newmobilenumber:
            return True
        else:
            return False

    def querymenber(self, status):
        # 切换至用户管理iframe                                                                                                                                                                                                                                                                                                                                                                                       elf.switch_frame(1)
        self.switch_frame('mainFrame')
        # 点击更多按钮
        self.find(By.CSS_SELECTOR, '.btnFormMore').click()
        # 状态选择正常
        self.finds(By.CSS_SELECTOR, '.select2-selection__arrow')[0].click()
        self.find(By.CSS_SELECTOR, '.select2-results__options>li:nth-child(2)').click()
        # 再点击更多按钮
        self.find(By.CSS_SELECTOR, '.btnFormMore').click()
        # 岗位选择总经理
        self.finds(By.CSS_SELECTOR, '.select2-selection__arrow')[1].click()
        self.find(By.CSS_SELECTOR, '.select2-results__options>li:nth-child(2)').click()
        time.sleep(1)
        # 点击查询按钮
        self.find(By.CSS_SELECTOR, '#searchForm>div:nth-child(7)>button:nth-child(1)').click()
        # 对面页面显示的数据状态是否正确
        newstatus = self.find(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[11]').get_attribute('innerText')
        if status == newstatus:
            return True
        else:
            return False






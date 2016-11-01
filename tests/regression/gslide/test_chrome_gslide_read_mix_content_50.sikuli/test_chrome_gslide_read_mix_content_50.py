# if you are putting your test script folders under {git project folder}/tests/, it will work fine.
# otherwise, you either add it to system path before you run or hard coded it in here.
sys.path.append(sys.argv[2])
import browser
import common
import gslide

com = common.General()
chrome = browser.Chrome()
gs = gslide.gSlide()

chrome.clickBar()
chrome.enterLink(sys.argv[3])
setAutoWaitTimeout(10)

sleep(2)
gs.wait_for_loaded()

type(Key.PAGE_DOWN)
sleep(1)
wait(gs.page_2)
type(Key.PAGE_DOWN)
sleep(1)
wait(gs.page_3)
type(Key.PAGE_DOWN)
sleep(1)
wait(gs.page_4)
type(Key.PAGE_DOWN)
sleep(1)
wait(gs.page_5)
type(Key.PAGE_DOWN)
sleep(1)
wait(gs.page_6)
type(Key.PAGE_DOWN)
sleep(1)
wait(gs.page_7)
type(Key.PAGE_DOWN)
sleep(1)
wait(gs.page_8)
type(Key.PAGE_DOWN)
sleep(1)
wait(gs.page_9)
type(Key.END)
sleep(1)
wait(gs.page_end)
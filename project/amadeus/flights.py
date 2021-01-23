import json
from datetime import *
from dateutil.tz import *
import time
import requests
# --------------------------------------------------------------------
name = "New York"
# lat2, lon2 = 51.5073, -0.127647
# --------------------------------------------------------------------

types = {
        'Clouds': '''
        <svg width="116" height="116" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg">
          <g id="clouds">
          <g id="Group">
          <g id="XMLID 239">
          <g id="Group_2">
          <g id="XMLID 1728">
          <g id="XMLID 1732">
          <g id="XMLID 1742">
          <g id="XMLID 1745">
          <g id="XMLID 1836">
          <g id="XMLID 1837">
          <g id="XMLID 1838">
          <g id="XMLID 1839">
          <g id="XMLID 1840">
          <g id="XMLID 1930">
          <g id="XMLID 1931">
          <g id="XMLID 1932">
          <g id="XMLID 1933">
          <g id="XMLID 1934">
          <path id="Vector" d="M256 512C397.385 512 512 397.385 512 256C512 114.615 397.385 0 256 0C114.615 0 0 114.615 0 256C0 397.385 114.615 512 256 512Z" fill="#4793FF"/>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          <g id="Group_3">
          <g id="XMLID 109">
          <g id="Group_4">
          <g id="XMLID 1594">
          <g id="XMLID 1597">
          <g id="XMLID 1598">
          <g id="XMLID 1599">
          <g id="XMLID 1600">
          <g id="XMLID 1602">
          <g id="XMLID 1687">
          <g id="XMLID 1689">
          <g id="XMLID 1720">
          <g id="XMLID 1721">
          <g id="XMLID 1722">
          <g id="XMLID 1723">
          <g id="XMLID 1724">
          <g id="XMLID 1726">
          <path id="Vector_2" d="M256 512C397.385 512 512 397.385 512 256C512 114.615 397.385 0 256 0C114.615 0 0 114.615 0 256C0 397.385 114.615 512 256 512Z" fill="#4793FF"/>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          <path id="Vector_3" d="M512 256C512 239.212 510.366 222.808 507.281 206.922L429.309 122.023C429.309 122.023 281 87 271 149.667C261 212.333 69.407 356.458 69.407 356.458L222.81 509.861C233.675 511.268 244.752 512 256 512C397.385 512 512 397.385 512 256Z" fill="#424FDD"/>
          <path id="Vector_4" d="M345.953 298.016C405.436 298.016 453.657 249.795 453.657 190.312C453.657 130.829 405.436 82.608 345.953 82.608C286.47 82.608 238.249 130.829 238.249 190.312C238.249 249.795 286.47 298.016 345.953 298.016Z" fill="#FFEA92"/>
          <path id="Vector_5" d="M453.66 190.31C453.66 249.8 405.44 298.02 345.95 298.02V82.61C405.44 82.61 453.66 130.83 453.66 190.31Z" fill="#FFDD50"/>
          <g id="Group_5">
          <g id="Group_6">
          <path id="Vector_6" d="M333.483 244.515C330.871 244.515 328.3 244.683 325.767 244.977C326.016 242.14 326.151 239.27 326.151 236.368C326.151 182.655 282.608 139.111 228.894 139.111C184.159 139.111 146.484 169.316 135.137 210.443C131.534 209.969 127.86 209.721 124.128 209.721C77.965 209.721 40.543 247.143 40.543 293.306C40.543 339.469 77.965 376.891 124.128 376.891H333.483C370.038 376.891 399.671 347.258 399.671 310.703C399.671 274.148 370.038 244.515 333.483 244.515Z" fill="white"/>
          <g id="Group_7">
          <path id="Vector_7" d="M399.671 310.7C399.671 347.257 370.039 376.889 333.482 376.889H220.107V139.504C223.002 139.238 225.932 139.109 228.896 139.109C282.611 139.109 326.153 182.651 326.153 236.366C326.153 239.27 326.016 242.139 325.766 244.975C328.3 244.683 330.869 244.511 333.481 244.511C370.039 244.51 399.671 274.151 399.671 310.7Z" fill="#DAEFEC"/>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </svg>
        ''',

        'Rain': '''
        <svg width="116" height="116" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg">
          <g id="rain">
          <g id="Group">
          <g id="XMLID 117">
          <g id="Group_2">
          <path id="Vector" d="M256 512C397.385 512 512 397.385 512 256C512 114.615 397.385 0 256 0C114.615 0 0 114.615 0 256C0 397.385 114.615 512 256 512Z" fill="#51EAF2"/>
          </g>
          </g>
          <path id="Vector_2" d="M512 256C512 250.338 511.796 244.724 511.434 239.154L350.622 78.342L83.856 290.17L155.161 361.838L129.328 452.666L175.844 499.182C201.061 507.49 228.002 512 256 512C397.385 512 512 397.385 512 256Z" fill="#22C2D3"/>
          <g id="Group_3">
          <path id="Vector_3" d="M386.228 160.74C383.228 160.74 380.275 160.933 377.366 161.271C377.652 158.012 377.807 154.716 377.807 151.382C377.807 89.6839 327.791 39.6689 266.094 39.6689C214.709 39.6689 171.434 74.3639 158.401 121.605C154.263 121.06 150.043 120.775 145.755 120.775C92.731 120.775 49.746 163.76 49.746 216.784C49.746 269.808 92.731 312.793 145.755 312.793H386.229C428.217 312.793 462.256 278.755 462.256 236.766C462.256 194.777 428.217 160.74 386.228 160.74Z" fill="#4793FF"/>
          <g id="Group_4">
          <path id="Vector_4" d="M462.255 236.764C462.255 278.755 428.218 312.792 386.227 312.792H256V40.121C259.326 39.815 262.691 39.667 266.096 39.667C327.795 39.667 377.809 89.681 377.809 151.38C377.809 154.716 377.651 158.012 377.365 161.268C380.276 160.933 383.227 160.735 386.227 160.735C428.218 160.735 462.255 194.782 462.255 236.764Z" fill="#424FDD"/>
          </g>
          </g>
          <g id="Group_5">
          <g id="Group_6">
          <path id="Vector_5" d="M278.224 350.634H308.224V452.667H278.224V350.634Z" fill="#DAEFEC"/>
          </g>
          <g id="Group_7">
          <path id="Vector_6" d="M352.671 350.634H382.671V413.236H352.671V350.634Z" fill="#DAEFEC"/>
          </g>
          <g id="Group_8">
          <path id="Vector_7" d="M129.329 350.634H159.329V452.667H129.329V350.634Z" fill="white"/>
          </g>
          <g id="Group_9">
          <path id="Vector_8" d="M203.776 350.634H233.776V413.236H203.776V350.634Z" fill="white"/>
          </g>
          </g>
          </g>
          </g>
        </svg>''',

        'Clear': '''
        <svg width="116" height="116" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg">
          <g id="clear">
          <g id="Group">
          <g id="XMLID 31">
          <g id="Group_2">
          <g id="XMLID 1100">
          <g id="XMLID 1101">
          <g id="XMLID 1102">
          <g id="XMLID 1103">
          <g id="XMLID 1104">
          <g id="XMLID 1105">
          <g id="XMLID 1106">
          <g id="XMLID 1107">
          <g id="XMLID 1108">
          <g id="XMLID 1109">
          <g id="XMLID 1307">
          <g id="XMLID 1371">
          <g id="XMLID 1618">
          <g id="XMLID 1740">
          <path id="Vector" d="M256 512C397.385 512 512 397.385 512 256C512 114.615 397.385 0 256 0C114.615 0 0 114.615 0 256C0 397.385 114.615 512 256 512Z" fill="#00337A"/>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          <path id="Vector_2" d="M512 256C512 235.756 509.64 216.065 505.198 197.176L410.011 101.989L347.5 128L256 38.196L243 181L38.195 256L147.25 363.75L101.988 410.011L197.175 505.198C216.065 509.64 235.756 512 256 512C397.385 512 512 397.385 512 256Z" fill="#002659"/>
          <path id="Vector_3" d="M473.807 256L472.478 255.15C444.729 237.403 437.24 200.176 455.969 173.08L456.866 171.782C424.218 166.111 402.898 134.352 410.013 101.988C377.001 109.246 344.555 87.6669 338.484 54.4169C311.389 73.4919 273.856 66.1109 256.003 38.1949L255.153 39.5239C237.406 67.2729 200.179 74.7619 173.083 56.0329L171.785 55.1359C166.114 87.7829 134.355 109.104 101.992 101.989L102.331 103.529C109.404 135.699 88.375 167.318 55.972 173.235L54.42 173.518C73.495 200.614 66.114 238.147 38.198 256L39.527 256.85C67.276 274.597 74.764 311.824 56.036 338.92L55.139 340.218C87.787 345.889 109.107 377.648 101.992 410.012L103.532 409.673C135.702 402.6 167.321 423.629 173.238 456.032L173.521 457.584C200.616 438.508 238.149 445.89 256.002 473.806L256.852 472.477C274.599 444.728 311.826 437.24 338.922 455.968L340.22 456.865C345.891 424.218 377.65 402.897 410.014 410.012L409.675 408.471C402.602 376.301 423.631 344.682 456.034 338.765L457.586 338.482C438.509 311.386 445.891 273.853 473.807 256Z" fill="#FFB522"/>
          <path id="Vector_4" d="M446.98 305.06C446.98 316.61 450.41 328.28 457.59 338.48L456.03 338.76C423.63 344.68 402.6 376.3 409.67 408.47L410.01 410.01C405.8 409.08 401.6 408.64 397.46 408.64C369.83 408.64 345.15 428.47 340.22 456.86L338.92 455.97C311.83 437.24 274.6 444.73 256.85 472.48L256 473.8V38.2C267.14 55.61 285.93 65.0299 305.06 65.0299C316.61 65.0299 328.28 61.5999 338.48 54.4199C343.76 83.3199 368.95 103.4 397.13 103.4C401.37 103.4 405.69 102.94 410.01 101.99C409.08 106.2 408.64 110.4 408.64 114.54C408.64 142.17 428.47 166.85 456.87 171.78L455.97 173.08C437.24 200.18 444.73 237.4 472.48 255.15L473.81 256C456.4 267.13 446.98 285.92 446.98 305.06Z" fill="#FD9827"/>
          <g id="Group_3">
          <g id="Group_4">
          <g id="XMLID 66">
          <g id="Group_5">
          <g id="XMLID 1111">
          <g id="XMLID 1112">
          <g id="XMLID 1113">
          <g id="XMLID 1160">
          <g id="XMLID 1170">
          <g id="XMLID 1171">
          <g id="XMLID 1282">
          <g id="XMLID 1283">
          <g id="XMLID 1506">
          <g id="XMLID 1586">
          <g id="XMLID 1587">
          <g id="XMLID 1588">
          <g id="XMLID 1589">
          <g id="XMLID 1590">
          <path id="Vector_5" d="M256 408.665C340.315 408.665 408.665 340.315 408.665 256C408.665 171.685 340.315 103.335 256 103.335C171.685 103.335 103.335 171.685 103.335 256C103.335 340.315 171.685 408.665 256 408.665Z" fill="#FFE05F"/>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          <g id="XMLID 70">
          <g id="Group_6">
          <g id="XMLID 1284">
          <g id="XMLID 1285">
          <g id="XMLID 1286">
          <g id="XMLID 1287">
          <g id="XMLID 1288">
          <g id="XMLID 1289">
          <g id="XMLID 1304">
          <g id="XMLID 1305">
          <g id="XMLID 1306">
          <g id="XMLID 1474">
          <g id="XMLID 1476">
          <g id="XMLID 1482">
          <g id="XMLID 1489">
          <g id="Group_7">
          <path id="Vector_6" d="M408.67 256C408.67 324.2 363.93 381.97 302.21 401.55C287.63 406.18 272.11 408.67 256 408.67V103.33C272.11 103.33 287.63 105.82 302.21 110.45C363.93 130.03 408.67 187.8 408.67 256Z" fill="#F9CB0D"/>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </svg>
        ''',

        'Drizzle': '''
        <svg width="116" height="116" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg">
          <g id="drizzle">
          <g id="Group">
          <g id="XMLID 112">
          <g id="Group_2">
          <g id="XMLID 1004">
          <g id="XMLID 1005">
          <g id="XMLID 1006">
          <g id="XMLID 1007">
          <g id="XMLID 1008">
          <g id="XMLID 1009">
          <g id="XMLID 1024">
          <g id="XMLID 1077">
          <g id="XMLID 1078">
          <g id="XMLID 1079">
          <g id="XMLID 1081">
          <g id="XMLID 1518">
          <g id="XMLID 1529">
          <g id="XMLID 1566">
          <path id="Vector" d="M256 512C397.385 512 512 397.385 512 256C512 114.615 397.385 0 256 0C114.615 0 0 114.615 0 256C0 397.385 114.615 512 256 512Z" fill="#00337A"/>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          <path id="Vector_2" d="M512 256C512 248.19 511.63 240.468 510.946 232.836L347.871 69.761L87.571 276.518L137.365 326.312C137.557 326.523 104.485 368.386 104.485 368.386L153.844 417.657L129.769 440.791L193.216 504.232C213.307 509.298 234.337 512 256 512C397.385 512 512 397.385 512 256Z" fill="#002659"/>
          <g id="Group_3">
          <g id="Group_4">
          <g id="Group_5">
          <g id="Group_6">
          <path id="Vector_3" d="M384.924 152.691C382 152.691 379.122 152.879 376.286 153.208C376.565 150.032 376.715 146.819 376.715 143.57C376.715 83.4379 327.968 34.6909 267.836 34.6909C217.755 34.6909 175.578 68.5059 162.875 114.547C158.842 114.016 154.729 113.738 150.55 113.738C98.871 113.738 56.977 155.632 56.977 207.311C56.977 258.99 98.871 300.884 150.55 300.884H384.923C425.846 300.884 459.021 267.709 459.021 226.786C459.021 185.863 425.847 152.691 384.924 152.691Z" fill="white"/>
          <g id="Group_7">
          <path id="Vector_4" d="M459.022 226.785C459.022 267.711 425.849 300.884 384.923 300.884H258V35.1319C261.241 34.8339 264.521 34.6899 267.84 34.6899C327.973 34.6899 376.719 83.4349 376.719 143.569C376.719 146.82 376.565 150.032 376.286 153.207C379.123 152.88 381.999 152.688 384.923 152.688C425.848 152.686 459.022 185.869 459.022 226.785Z" fill="#DAEFEC"/>
          </g>
          </g>
          </g>
          <g id="Group_8">
          <path id="Vector_5" d="M141.637 325.801V351.927C141.637 361.013 136.105 369.184 127.669 372.559C118.112 376.382 107.18 373.14 101.251 364.726C93.682 353.983 98.808 338.982 111.368 335.117L141.637 325.801Z" fill="#51EAF2"/>
          <path id="Vector_6" d="M227.975 325.801V351.927C227.975 361.013 222.443 369.184 214.007 372.559C204.45 376.382 193.518 373.14 187.589 364.726C180.02 353.983 185.146 338.982 197.706 335.117L227.975 325.801Z" fill="#51EAF2"/>
          <g id="Group_9">
          <path id="Vector_7" d="M314.314 325.801V351.927C314.314 361.013 308.782 369.184 300.346 372.559C290.789 376.382 279.857 373.14 273.928 364.726C266.359 353.983 271.485 338.982 284.045 335.117L314.314 325.801Z" fill="#22C2D3"/>
          <path id="Vector_8" d="M400.652 325.801V351.927C400.652 361.013 395.12 369.184 386.684 372.559C377.127 376.382 366.195 373.14 360.266 364.726C352.697 353.983 357.823 338.982 370.383 335.117L400.652 325.801Z" fill="#22C2D3"/>
          </g>
          </g>
          </g>
          <path id="Vector_9" d="M167.386 398.641V424.767C167.386 433.853 161.854 442.024 153.418 445.399C143.861 449.222 132.929 445.98 127 437.566C119.431 426.823 124.557 411.822 137.117 407.957L167.386 398.641Z" fill="#51EAF2"/>
          <path id="Vector_10" d="M253.724 398.641V424.767C253.724 433.853 248.192 442.024 239.756 445.399C230.199 449.222 219.267 445.98 213.338 437.566C205.769 426.823 210.895 411.822 223.455 407.957L253.724 398.641Z" fill="#51EAF2"/>
          <path id="Vector_11" d="M340.062 398.641V424.767C340.062 433.853 334.53 442.024 326.094 445.399C316.537 449.222 305.605 445.98 299.676 437.566C292.107 426.823 297.233 411.822 309.793 407.957L340.062 398.641Z" fill="#22C2D3"/>
          </g>
          </g>
          </g>
          </svg>''',

        'Haze': '''
        <svg width="116" height="116" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg">
          <g id="haze">
          <g id="Group">
          <g id="XMLID 568">
          <g id="Group_2">
          <g id="XMLID 1372">
          <g id="XMLID 1373">
          <g id="XMLID 1374">
          <g id="XMLID 1375">
          <g id="XMLID 1376">
          <g id="XMLID 1377">
          <g id="XMLID 1378">
          <g id="XMLID 1405">
          <g id="XMLID 1406">
          <g id="XMLID 1407">
          <g id="XMLID 1408">
          <g id="XMLID 1409">
          <g id="XMLID 1410">
          <g id="XMLID 1427">
          <path id="Vector" d="M256 512C397.385 512 512 397.385 512 256C512 114.615 397.385 0 256 0C114.615 0 0 114.615 0 256C0 397.385 114.615 512 256 512Z" fill="#00337A"/>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          <path id="Vector_2" d="M512 256C512 242.323 510.915 228.9 508.85 215.804L397.025 103.631L329.1 107.833L321.111 129.338L387 194C387 194 63.124 228.309 59.395 243.154L320.09 503.91C430.459 475.46 512 375.253 512 256V256Z" fill="#002659"/>
          <g id="Group_3">
          <g id="Group_4">
          <g id="Group_5">
          <g id="Group_6">
          <path id="Vector_3" d="M335.781 243.154H59.395V196.528H335.78C352.386 196.528 366.932 185.311 371.151 169.25C374.908 154.949 369.749 139.902 358.008 130.915C347.301 122.719 332.475 122.087 321.11 129.337L296.033 90.03C323.85 72.283 360.145 73.835 386.347 93.89C413.057 114.334 424.792 148.564 416.246 181.094C406.649 217.635 373.559 243.154 335.781 243.154V243.154Z" fill="#51EAF2"/>
          </g>
          </g>
          <g id="Group_7">
          <path id="Vector_4" d="M337.144 422.345C324.87 422.345 312.569 418.895 301.792 411.928L327.103 372.77C333.707 377.04 342.329 376.661 348.557 371.831C355.816 366.202 358.993 356.732 356.653 347.706C354.061 337.71 345.218 330.727 335.149 330.727H146.901V284.102H335.15C366.462 284.102 393.864 305.445 401.787 336.004C408.808 363.087 399.131 391.611 377.134 408.673C365.428 417.752 351.303 422.343 337.144 422.345V422.345Z" fill="#51EAF2"/>
          </g>
          </g>
          <g id="Group_8">
          <g id="Group_9">
          <g id="Group_10">
          <path id="Vector_5" d="M416.25 181.1C406.65 217.64 373.56 243.15 335.78 243.15H239.2V196.53H335.78C352.39 196.53 366.93 185.31 371.15 169.25C374.91 154.95 369.75 139.9 358.01 130.92C347.3 122.72 332.48 122.09 321.11 129.34L296.03 90.03C323.85 72.28 360.15 73.84 386.35 93.89C413.06 114.34 424.79 148.57 416.25 181.1V181.1Z" fill="#24CEE0"/>
          </g>
          </g>
          <g id="Group_11">
          <path id="Vector_6" d="M377.13 408.67C365.43 417.75 351.3 422.34 337.14 422.34C324.87 422.34 312.57 418.89 301.79 411.93L327.1 372.77C333.71 377.04 342.33 376.66 348.56 371.83C355.82 366.2 358.99 356.73 356.65 347.71C354.06 337.71 345.22 330.73 335.15 330.73H239.2V284.1H335.15C366.46 284.1 393.86 305.45 401.79 336C408.81 363.09 399.13 391.61 377.13 408.67V408.67Z" fill="#24CEE0"/>
          </g>
          </g>
          </g>
          </g>
          </g>
          </svg>''',


        'Snow': '''
        <svg width="116" height="116" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg">
          <g id="snow">
          <g id="Group">
          <g id="XMLID 29">
          <g id="Group_2">
          <g id="XMLID 1939">
          <g id="XMLID 1941">
          <g id="XMLID 1942">
          <g id="XMLID 1943">
          <g id="XMLID 1944">
          <g id="XMLID 1945">
          <g id="XMLID 1946">
          <g id="XMLID 1947">
          <g id="XMLID 1948">
          <g id="XMLID 1949">
          <g id="XMLID 1950">
          <g id="XMLID 1951">
          <g id="XMLID 1952">
          <g id="XMLID 1953">
          <path id="Vector" d="M256 512C397.385 512 512 397.385 512 256C512 114.615 397.385 0 256 0C114.615 0 0 114.615 0 256C0 397.385 114.615 512 256 512Z" fill="#4793FF"/>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          <path id="Vector_2" d="M512 256C512 246.655 511.485 237.431 510.509 228.346L347.148 64.985L86.795 271.795L149.359 335.893L120.111 371.997L169.384 421.283C161.052 424.818 153.022 449.8 153.022 449.8L211.331 508.109C225.836 510.661 240.761 512 256 512C397.385 512 512 397.385 512 256Z" fill="#424FDD"/>
          <g id="Group_3">
          <g id="Group_4">
          <g id="Group_5">
          <path id="Vector_3" d="M384.924 148.691C382 148.691 379.122 148.879 376.286 149.208C376.565 146.032 376.715 142.819 376.715 139.57C376.715 79.4379 327.968 30.6909 267.836 30.6909C217.755 30.6909 175.578 64.5059 162.875 110.548C158.842 110.017 154.729 109.739 150.55 109.739C98.871 109.739 56.9771 151.633 56.9771 203.312C56.9771 254.991 98.871 296.885 150.55 296.885H384.923C425.846 296.885 459.021 263.71 459.021 222.787C459.021 181.864 425.847 148.691 384.924 148.691V148.691Z" fill="white"/>
          <g id="Group_6">
          <path id="Vector_4" d="M459.022 222.785C459.022 263.711 425.849 296.884 384.923 296.884H258V31.1319C261.241 30.8339 264.521 30.6899 267.839 30.6899C327.972 30.6899 376.718 79.4349 376.718 139.569C376.718 142.82 376.564 146.032 376.285 149.207C379.122 148.88 381.998 148.688 384.922 148.688C425.848 148.686 459.022 181.869 459.022 222.785V222.785Z" fill="#DAEFEC"/>
          </g>
          </g>
          </g>
          <g id="Group_7">
          <path id="Vector_5" d="M156.865 357.087C158.907 344.413 150.288 332.484 137.614 330.442C124.94 328.401 113.011 337.02 110.969 349.693C108.928 362.367 117.547 374.296 130.22 376.338C142.894 378.38 154.823 369.761 156.865 357.087Z" fill="white"/>
          <path id="Vector_6" d="M245.933 357.112C247.975 344.438 239.356 332.509 226.682 330.467C214.009 328.426 202.079 337.045 200.038 349.718C197.996 362.392 206.615 374.321 219.289 376.363C231.962 378.404 243.892 369.785 245.933 357.112Z" fill="white"/>
          <g id="Group_8">
          <path id="Vector_7" d="M335.264 357.513C337.498 344.865 329.056 332.801 316.408 330.566C303.76 328.332 291.696 336.774 289.461 349.422C287.227 362.07 295.669 374.135 308.317 376.369C320.965 378.603 333.03 370.161 335.264 357.513Z" fill="#DAEFEC"/>
          <path id="Vector_8" d="M424.075 357.054C426.13 344.381 417.521 332.441 404.847 330.387C392.174 328.332 380.234 336.941 378.18 349.614C376.125 362.288 384.734 374.228 397.407 376.282C410.081 378.337 422.021 369.728 424.075 357.054Z" fill="#DAEFEC"/>
          </g>
          </g>
          <g id="Group_9">
          <path id="Vector_9" d="M189.753 434.895C191.795 422.222 183.176 410.292 170.502 408.251C157.829 406.209 145.9 414.828 143.858 427.502C141.816 440.175 150.435 452.105 163.109 454.146C175.783 456.188 187.712 447.569 189.753 434.895Z" fill="white"/>
          <path id="Vector_10" d="M278.864 434.831C280.918 422.157 272.31 410.217 259.636 408.163C246.962 406.108 235.023 414.717 232.968 427.391C230.914 440.064 239.522 452.004 252.196 454.058C264.87 456.113 276.809 447.504 278.864 434.831Z" fill="white"/>
          <path id="Vector_11" d="M367.919 434.839C369.974 422.165 361.365 410.225 348.691 408.171C336.018 406.116 324.078 414.725 322.024 427.399C319.969 440.072 328.578 452.012 341.251 454.066C353.925 456.121 365.865 447.512 367.919 434.839Z" fill="#DAEFEC"/>
          </g>
          <path id="Vector_12" d="M279.25 431.17C279.25 444.01 268.84 454.42 256 454.42V407.92C268.84 407.92 279.25 418.33 279.25 431.17Z" fill="#DAEFEC"/>
          </g>
          </g>
          </g>
          </svg>''',

        'Thunderstorm': '''
        <svg width="116" height="116" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg">
          <g id="thunderstorm">
          <g id="Group">
          <g id="XMLID 45">
          <g id="Group_2">
          <g id="XMLID 961">
          <g id="XMLID 980">
          <g id="XMLID 989">
          <g id="XMLID 1082">
          <g id="XMLID 1083">
          <g id="XMLID 1084">
          <g id="XMLID 1099">
          <g id="XMLID 1114">
          <g id="XMLID 1325">
          <g id="XMLID 1326">
          <g id="XMLID 1327">
          <g id="XMLID 1328">
          <g id="XMLID 1329">
          <g id="XMLID 1330">
          <path id="Vector" d="M256 512C397.385 512 512 397.385 512 256C512 114.615 397.385 0 256 0C114.615 0 0 114.615 0 256C0 397.385 114.615 512 256 512Z" fill="#51EAF2"/>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          </g>
          <path id="Vector_2" d="M512 256C512 239.806 510.479 223.97 507.604 208.61L374.695 75.701L341.234 162.979L298.279 120.024L64.249 305.894L194.784 436.637L183.931 456.151L239.218 511.439C244.768 511.798 250.36 512 256 512C397.385 512 512 397.385 512 256V256Z" fill="#22C2D3"/>
          <g id="Group_3">
          <path id="Vector_3" d="M405.606 144.043C403.224 144.043 400.879 144.196 398.57 144.465C398.797 141.878 398.92 139.26 398.92 136.614C398.92 87.63 359.21 47.92 310.226 47.92C269.43 47.92 235.072 75.466 224.724 112.972C221.438 112.54 218.088 112.313 214.684 112.313C172.586 112.313 138.458 146.44 138.458 188.539C138.458 230.637 172.586 264.765 214.684 264.765H405.607C438.943 264.765 465.968 237.74 465.968 204.404C465.968 171.068 438.943 144.043 405.606 144.043V144.043Z" fill="#00337A"/>
          <g id="Group_4">
          <g id="Group_5">
          <path id="Vector_4" d="M465.967 204.401C465.967 237.74 438.944 264.763 405.605 264.763H302.212V48.277C304.853 48.034 307.524 47.917 310.227 47.917C359.212 47.917 398.921 87.625 398.921 136.611C398.921 139.259 398.796 141.876 398.568 144.462C400.879 144.196 403.222 144.039 405.604 144.039C438.944 144.039 465.967 171.07 465.967 204.401V204.401Z" fill="#002659"/>
          </g>
          </g>
          </g>
          <g id="Group_6">
          <g id="Group_7">
          <path id="Vector_5" d="M330.689 193.608C328.059 193.608 325.47 193.777 322.92 194.073C323.171 191.216 323.306 188.326 323.306 185.404C323.306 131.317 279.46 87.4709 225.373 87.4709C180.327 87.4709 142.39 117.886 130.964 159.299C127.336 158.822 123.636 158.572 119.878 158.572C73.395 158.572 35.712 196.254 35.712 242.738C35.712 289.222 73.394 326.904 119.878 326.904H330.689C367.498 326.904 397.337 297.064 397.337 260.256C397.337 223.447 367.498 193.608 330.689 193.608V193.608Z" fill="#4793FF"/>
          <g id="Group_8">
          <path id="Vector_6" d="M397.337 260.253C397.337 297.064 367.499 326.903 330.687 326.903H216.525V87.867C219.44 87.599 222.391 87.469 225.375 87.469C279.463 87.469 323.308 131.314 323.308 185.402C323.308 188.326 323.17 191.216 322.919 194.071C325.471 193.777 328.058 193.604 330.688 193.604C367.499 193.603 397.337 223.45 397.337 260.253V260.253Z" fill="#424FDD"/>
          </g>
          </g>
          <path id="Vector_7" d="M277.013 291.015H189.47L138.457 379.985H202.145L183.932 456.151L277.013 354.597H240.854L277.013 291.015Z" fill="#FFE05F"/>
          <path id="Vector_8" d="M419.556 247H332.013L281 335.97H344.688L326.475 412.136L419.556 310.582H383.397L419.556 247Z" fill="#FFE05F"/>
          <path id="Vector_9" d="M240.852 354.6H277.013L216.525 420.594V291.017H277.013L240.852 354.6Z" fill="#F9CB0D"/>
          </g>
          </g>
          </g>
          </svg>
          ''',
        'Night': '''
        <svg width="116" height="116" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg">
          <g id="night">
          <g id="Group">
          <g id="XMLID 17">
          <g id="Group_2">
          <g id="Group_3">
          <path id="Vector" d="M256 512C397.385 512 512 397.385 512 256C512 114.615 397.385 0 256 0C114.615 0 0 114.615 0 256C0 397.385 114.615 512 256 512Z" fill="#4793FF"/>
          </g>
          </g>
          </g>
          <g id="Group_4">
          <path id="Vector_2" d="M512 256C512 249.472 511.752 243.001 511.272 236.596L382.239 107.563L349.462 96.0559C252.423 61.9899 149.884 130.74 144.548 233.447L135.521 407.184L268.564 511.69C404.112 505.139 512 393.172 512 256V256Z" fill="#424FDD"/>
          <g id="Group_5">
          <path id="Vector_3" d="M208.208 251.963C208.208 171.666 277.981 106.572 364.051 106.572C370.205 106.572 376.272 106.916 382.24 107.563C347.823 76.578 302.278 57.715 252.323 57.715C145.042 57.715 58.074 144.683 58.074 251.964C58.074 359.245 145.042 446.213 252.323 446.213C302.278 446.213 347.823 427.349 382.24 396.365C376.272 397.012 370.205 397.356 364.051 397.356C277.981 397.354 208.208 332.26 208.208 251.963V251.963Z" fill="#FFF4C5"/>
          <g id="Group_6">
          <path id="Vector_4" d="M364.05 397.352C370.203 397.352 376.274 397.015 382.243 396.362C347.827 427.35 302.278 446.216 252.322 446.216C248.904 446.216 245.496 446.124 242.119 445.951V342.519C270.668 375.935 314.686 397.352 364.05 397.352Z" fill="#FFEA92"/>
          <path id="Vector_5" d="M242.119 161.407V57.975C245.496 57.802 248.904 57.71 252.322 57.71C302.278 57.71 347.827 76.576 382.243 107.564C376.274 106.911 370.203 106.574 364.05 106.574C314.686 106.574 270.668 127.991 242.119 161.407V161.407Z" fill="#FFEA92"/>
          </g>
          </g>
          </g>
          </g>
          </g>
          </svg>'''
    }
def weather(city_name):
    API_KEY = '701726f03e98fea267e17f9e15b584f0'
    link = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
    r = requests.get(link).json()
    if r['weather'][0]['main'] not in types.keys():
      if int(str(datetime.now(tzoffset("", r['timezone']))).split(" ")[1][:8][:2]) > 20:
        svg_name = types['Night']
      else:
        svg_name = types['Clear']
    else:
      svg_name = types[r['weather'][0]['main']]
    sample = {
        'name': r['name'],
        'coor': [r['coord']['lon'], r['coord']['lat']],
        'main_weather_type': r['weather'][0]['main'],
        'svg' : svg_name,
        'current_temp': int(r['main']['temp'] - 273),
        'min_temp': int(r['main']['temp_min'] - 273),
        'max_temp': int(r['main']['temp_max'] - 273),
        'pressure': r['main']['pressure'],
        'humidity': r['main']['humidity'],
        'visibility': r['visibility'],
        'wind': [r['wind']['speed'], r['wind']['deg']],
        'dt': r['dt'],
        'country': r['sys']['country'],
        'sun_time': [r['sys']['sunrise'], r['sys']['sunset']],
        'timezone': r['timezone'],
        'date': str(datetime.now(tzoffset("", r['timezone']))).split(" ")[0],
        'time': str(datetime.now(tzoffset("", r['timezone']))).split(" ")[1][:8]
    }
    return sample

# print(weather(name))
# print()
# --------------------------------------------------------------------

# Airport Nearest Relevant


def nearest_airport(lat, lon, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = f'https://test.api.amadeus.com/v1/reference-data/locations/airports?latitude={lat}&longitude={lon}'

    response = requests.get(url, headers=headers)
    data = response.json()['data']
    min = data[0]['distance']['value']
    min_loc = data[0]
    for location in data:
        if location['distance']['value'] < min:
            min = location['distance']['value']
            min_loc = location
    # print("{} - {}{}".format(min_loc['name'],min_loc['distance']['value'],min_loc['distance']['unit']))
    # print(min_loc['address']['cityCode'])
    return min_loc['address']['cityCode'], min_loc['name']

# --------------------------------------------------------------------
# Flight Inspiration Search


def flight_search(lat1, lon1, lat2, lon2, departure_date, return_date, token):
  start = time.time()
  # try:
  headers = {
      "Authorization": f"Bearer {token}"
  }
  import asyncio
  import aiohttp

  async def main():
    async with aiohttp.ClientSession() as session:
      tasks = []
      task1 = asyncio.ensure_future(get_it(session, lat1, lon1, token))
      task2 = asyncio.ensure_future(get_it(session, lat2, lon2, token))

      tasks.append(task1)
      tasks.append(task2)

      final = await asyncio.gather(*tasks)
    return final

  async def get_it(session, lat, lon, token):
    url = f'https://test.api.amadeus.com/v1/reference-data/locations/airports?latitude={lat}&longitude={lon}'
    async with session.get(url, headers=headers) as response:
      data = await response.json()
      try:
        data = data['data']
        min = data[0]['distance']['value']
        min_loc = data[0]
        for location in data:
            if location['distance']['value'] < min:
                min = location['distance']['value']
                min_loc = location
      # print("{} - {}{}".format(min_loc['name'],min_loc['distance']['value'],min_loc['distance']['unit']))
      # print(min_loc['address']['cityCode'])
        return [min_loc['address']['cityCode'], min_loc['name']]
      except:
        return False, False


  # city1, airport_name1 = nearest_airport(lat1, lon1, token)
  # city2, airport_name2 = nearest_airport(lat2, lon2, token)
  # ****************DONT CLEAR THIS****************
  # TESTING DATES
  # departure_date = '2021-01-20'
  # return_date = '2021-01-27'

  # INITIAL CODE STARTS
  # url = f"https://test.api.amadeus.com/v1/shopping/flight-destinations?origin={city1}&departureDate={departure_date}"
  # response = requests.get(url, headers=headers)
  # data = response.json()['data']
  # for flight in data:
  #     if flight['destination'] == city2:
  #         data_str = json.dumps(flight, indent=3)
  #         print(data_str)
  #         print("\nSEPARATOR\n")
  # INITIAL CODE ENDS
  # ****************DONT CLEAR THIS****************
  [city1, airport_name1],[city2, airport_name2] = asyncio.run(main())
  url = f"https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode={city1}&destinationLocationCode={city2}&departureDate={departure_date}&returnDate={return_date}&adults=2&max=6"

  response = requests.get(url, headers=headers)
  data = response.json().get('data', 'DataError')
  # print(data)
  # print("\n\n\n")
  print(time.time() - start)
  return data, airport_name1, airport_name2
  # except:
      # print(time.time() - start)
      # return False, False, False
  # return data_str

# --------------------------------------------------------------------


def check_in(code, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    print(f"NAHI\n\n{code}\n\n")
    url = f'https://test.api.amadeus.com/v2/reference-data/urls/checkin-links?airlineCode={code}'
    response = requests.get(url, headers=headers).json()['data'][0]['href']
    return response
# --------------------------------------------------------------------
# Airline CODE => LOGO, LINK


def lonk(code):
    dict = {
        "AI": ["Air India", "http://www.airindia.in/"],
        "AF": ["Air France", "http://www.airindia.in/"],
        "AK": ["Air Asia", "http://www.airindia.in/"],
        "BA": ["British Airways", "http://www.airindia.in/"],
        "DL": ["Delta", "http://www.airindia.in/"],
        "U2": ["EasyJet", "http://www.airindia.in/"],
        "EK": ["Emirates", "http://www.airindia.in/"],
        "G8": ["Go Air", "http://www.airindia.in/"],
        "6E": ["Indigo", "http://www.airindia.in/"],
        "9W": ["Jet Airways", "http://www.airindia.in/"],
        "LH": ["Lufthansa", "http://www.airindia.in/"],
        "NH": ["Nippon Airlines", "http://www.airindia.in/"],
        "SG": ["Spicejet", "http://www.airindia.in/"],
        "UA": ["United Airlines", "http://www.airindia.in/"],
        "IB": ["Iberia", "http://www.airindia.in/"]
    }
    return dict[code]


def website(code):
    url = "https://iata-and-icao-codes.p.rapidapi.com/airline"

    querystring = {"iata_code": code}

    headers = {
        'x-rapidapi-key': "b2c5d09d95msh761f4b7db94c313p17bff8jsn371b13a76e87",
        'x-rapidapi-host': "iata-and-icao-codes.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.json()[0]['website']

# --------------------------------------------------------------------
# Flight Offers Search


# def flight_offer_search(city1, city2, departure_date, return_date):
#     url = f"https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode={city1}&destinationLocationCode={city2}&departureDate={departure_date}&returnDate={return_date}&adults=2&max=5"
#     headers = {
#         "Authorization": f"Bearer {token}"
#     }

#     response = requests.get(url, headers=headers)
#     print(response.text)

# flight_offer_search()


# --------------------------------------------------------------------
# Airport & City Search by Keyword
# def airport(code, token):
#     import json
#     headers = {
#         "Authorization": f"Bearer {token}"
#     }
#     url = f'https://test.api.amadeus.com/v1/reference-data/locations?subType=CITY,AIRPORT&keyword={code}'
#     response = requests.get(url, headers=headers)
#     data = response.json()
#     print("\n\n\n")
#     print(json.dumps(data, indent=3))
    # return data[0]['name']


# print(airport("DEL"))

# --------------------------------------------------------------------

# Airline Code Lookup
def airline(code, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = f'https://test.api.amadeus.com/v1/reference-data/airlines?airlineCodes={code}'
    response = requests.get(url, headers=headers)
    response_str = response.json()['data'][0]['businessName']
    return response_str

# --------------------------------------------------------------------


'''
SAMPLE FLIGHT OFFER SEARCH
{
   "type": "flight-destination",
   "origin": "DEL",
   "destination": "BOM",
   "departureDate": "2021-01-20",
   "returnDate": "2021-01-21",
   "price": {
      "total": "7961.00"
   },
   "links": {
      "flightDates": "https://test.api.amadeus.com/v1/shopping/flight-dates?origin=DEL&destination=BOM&departureDate=2021-01-20&oneWay=false&duration=1,15&nonStop=false&viewBy=DURATION",
      "flightOffers": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=DEL&destinationLocationCode=BOM&departureDate=2021-01-20&returnDate=2021-01-21&adults=1&nonStop=false"
   }
}

SEPARATOR

{
  "meta" : {
    "count" : 5,
    "links" : {
      "self" : "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=DEL&destinationLocationCode=BOM&departureDate=2021-01-20&returnDate=2021-01-27&adults=2&max=5"
    }
  },
  "data" : [ {
    "type" : "flight-offer",
    "id" : "1",
    "source" : "GDS",
    "instantTicketingRequired" : false,
    "nonHomogeneous" : false,
    "oneWay" : false,
    "lastTicketingDate" : "2021-01-20",
    "numberOfBookableSeats" : 3,
    "itineraries" : [ {
      "duration" : "PT2H10M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-20T06:50:00"
        },
        "arrival" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-20T09:00:00"
        },
        "carrierCode" : "AI",
        "number" : "887",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H10M",
        "id" : "1",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    }, {
      "duration" : "PT2H15M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-27T07:00:00"
        },
        "arrival" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-27T09:15:00"
        },
        "carrierCode" : "AI",
        "number" : "866",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H15M",
        "id" : "3",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    } ],
    "price" : {
      "currency" : "EUR",
      "total" : "195.62",
      "base" : "164.00",
      "fees" : [ {
        "amount" : "0.00",
        "type" : "SUPPLIER"
      }, {
        "amount" : "0.00",
        "type" : "TICKETING"
      } ],
      "grandTotal" : "195.62"
    },
    "pricingOptions" : {
      "fareType" : [ "PUBLISHED" ],
      "includedCheckedBagsOnly" : true
    },
    "validatingAirlineCodes" : [ "AI" ],
    "travelerPricings" : [ {
      "travelerId" : "1",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "1",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "3",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    }, {
      "travelerId" : "2",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "1",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "3",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    } ]
  }, {
    "type" : "flight-offer",
    "id" : "2",
    "source" : "GDS",
    "instantTicketingRequired" : false,
    "nonHomogeneous" : false,
    "oneWay" : false,
    "lastTicketingDate" : "2021-01-20",
    "numberOfBookableSeats" : 3,
    "itineraries" : [ {
      "duration" : "PT2H10M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-20T06:50:00"
        },
        "arrival" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-20T09:00:00"
        },
        "carrierCode" : "AI",
        "number" : "887",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H10M",
        "id" : "1",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    }, {
      "duration" : "PT2H15M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-27T21:00:00"
        },
        "arrival" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-27T23:15:00"
        },
        "carrierCode" : "AI",
        "number" : "538",
        "aircraft" : {
          "code" : "77W"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H15M",
        "id" : "5",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    } ],
    "price" : {
      "currency" : "EUR",
      "total" : "195.62",
      "base" : "164.00",
      "fees" : [ {
        "amount" : "0.00",
        "type" : "SUPPLIER"
      }, {
        "amount" : "0.00",
        "type" : "TICKETING"
      } ],
      "grandTotal" : "195.62"
    },
    "pricingOptions" : {
      "fareType" : [ "PUBLISHED" ],
      "includedCheckedBagsOnly" : true
    },
    "validatingAirlineCodes" : [ "AI" ],
    "travelerPricings" : [ {
      "travelerId" : "1",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "1",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "5",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    }, {
      "travelerId" : "2",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "1",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "5",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    } ]
  }, {
    "type" : "flight-offer",
    "id" : "3",
    "source" : "GDS",
    "instantTicketingRequired" : false,
    "nonHomogeneous" : false,
    "oneWay" : false,
    "lastTicketingDate" : "2021-01-20",
    "numberOfBookableSeats" : 3,
    "itineraries" : [ {
      "duration" : "PT2H10M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-20T06:50:00"
        },
        "arrival" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-20T09:00:00"
        },
        "carrierCode" : "AI",
        "number" : "887",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H10M",
        "id" : "1",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    }, {
      "duration" : "PT2H15M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-27T10:00:00"
        },
        "arrival" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-27T12:15:00"
        },
        "carrierCode" : "AI",
        "number" : "809",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H15M",
        "id" : "4",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    } ],
    "price" : {
      "currency" : "EUR",
      "total" : "195.62",
      "base" : "164.00",
      "fees" : [ {
        "amount" : "0.00",
        "type" : "SUPPLIER"
      }, {
        "amount" : "0.00",
        "type" : "TICKETING"
      } ],
      "grandTotal" : "195.62"
    },
    "pricingOptions" : {
      "fareType" : [ "PUBLISHED" ],
      "includedCheckedBagsOnly" : true
    },
    "validatingAirlineCodes" : [ "AI" ],
    "travelerPricings" : [ {
      "travelerId" : "1",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "1",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "4",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    }, {
      "travelerId" : "2",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "1",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "4",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    } ]
  }, {
    "type" : "flight-offer",
    "id" : "4",
    "source" : "GDS",
    "instantTicketingRequired" : false,
    "nonHomogeneous" : false,
    "oneWay" : false,
    "lastTicketingDate" : "2021-01-20",
    "numberOfBookableSeats" : 5,
    "itineraries" : [ {
      "duration" : "PT2H15M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-20T10:40:00"
        },
        "arrival" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-20T12:55:00"
        },
        "carrierCode" : "AI",
        "number" : "865",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H15M",
        "id" : "2",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    }, {
      "duration" : "PT2H15M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-27T07:00:00"
        },
        "arrival" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-27T09:15:00"
        },
        "carrierCode" : "AI",
        "number" : "866",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H15M",
        "id" : "3",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    } ],
    "price" : {
      "currency" : "EUR",
      "total" : "195.62",
      "base" : "164.00",
      "fees" : [ {
        "amount" : "0.00",
        "type" : "SUPPLIER"
      }, {
        "amount" : "0.00",
        "type" : "TICKETING"
      } ],
      "grandTotal" : "195.62"
    },
    "pricingOptions" : {
      "fareType" : [ "PUBLISHED" ],
      "includedCheckedBagsOnly" : true
    },
    "validatingAirlineCodes" : [ "AI" ],
    "travelerPricings" : [ {
      "travelerId" : "1",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "2",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "3",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    }, {
      "travelerId" : "2",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "2",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "3",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    } ]
  }, {
    "type" : "flight-offer",
    "id" : "5",
    "source" : "GDS",
    "instantTicketingRequired" : false,
    "nonHomogeneous" : false,
    "oneWay" : false,
    "lastTicketingDate" : "2021-01-20",
    "numberOfBookableSeats" : 5,
    "itineraries" : [ {
      "duration" : "PT2H15M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-20T10:40:00"
        },
        "arrival" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-20T12:55:00"
        },
        "carrierCode" : "AI",
        "number" : "865",
        "aircraft" : {
          "code" : "32B"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H15M",
        "id" : "2",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    }, {
      "duration" : "PT2H15M",
      "segments" : [ {
        "departure" : {
          "iataCode" : "BOM",
          "terminal" : "2",
          "at" : "2021-01-27T21:00:00"
        },
        "arrival" : {
          "iataCode" : "DEL",
          "terminal" : "3",
          "at" : "2021-01-27T23:15:00"
        },
        "carrierCode" : "AI",
        "number" : "538",
        "aircraft" : {
          "code" : "77W"
        },
        "operating" : {
          "carrierCode" : "AI"
        },
        "duration" : "PT2H15M",
        "id" : "5",
        "numberOfStops" : 0,
        "blacklistedInEU" : false
      } ]
    } ],
    "price" : {
      "currency" : "EUR",
      "total" : "195.62",
      "base" : "164.00",
      "fees" : [ {
        "amount" : "0.00",
        "type" : "SUPPLIER"
      }, {
        "amount" : "0.00",
        "type" : "TICKETING"
      } ],
      "grandTotal" : "195.62"
    },
    "pricingOptions" : {
      "fareType" : [ "PUBLISHED" ],
      "includedCheckedBagsOnly" : true
    },
    "validatingAirlineCodes" : [ "AI" ],
    "travelerPricings" : [ {
      "travelerId" : "1",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "2",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "5",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    }, {
      "travelerId" : "2",
      "fareOption" : "STANDARD",
      "travelerType" : "ADULT",
      "price" : {
        "currency" : "EUR",
        "total" : "97.81",
        "base" : "82.00"
      },
      "fareDetailsBySegment" : [ {
        "segmentId" : "2",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      }, {
        "segmentId" : "5",
        "cabin" : "ECONOMY",
        "fareBasis" : "SIP",
        "class" : "S",
        "includedCheckedBags" : {
          "weight" : 25,
          "weightUnit" : "KG"
        }
      } ]
    } ]
  } ],
  "dictionaries" : {
    "locations" : {
      "BOM" : {
        "cityCode" : "BOM",
        "countryCode" : "IN"
      },
      "DEL" : {
        "cityCode" : "DEL",
        "countryCode" : "IN"
      }
    },
    "aircraft" : {
      "32B" : "AIRBUS A321 (SHARKLETS)",
      "77W" : "BOEING 777-300ER"
    },
    "currencies" : {
      "EUR" : "EURO"
    },
    "carriers" : {
      "AI" : "AIR INDIA"
    }
  }
}

'''

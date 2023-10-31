"""Order Email Template"""


def generate_email(data: dict):
    """Generate Order Success Email"""
    html_email = """
        <!DOCTYPE html
            PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"
            style="font-family:arial, 'helvetica neue', helvetica, sans-serif">

        <head>
            <meta charset="UTF-8">
            <meta content="width=device-width, initial-scale=1" name="viewport">
            <meta name="x-apple-disable-message-reformatting">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta content="telephone=no" name="format-detection">
            <title>Kumpe3D Order Confirmation</title><!--[if (mso 16)]>
        <style type="text/css">
        a {text-decoration: none;}
        </style>
        <![endif]--><!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]--><!--[if gte mso 9]>
        <xml>
        <o:OfficeDocumentSettings>
        <o:AllowPNG></o:AllowPNG>
        <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
        </xml>
        <![endif]--><!--[if !mso]><!-- -->
            <link href="https://fonts.googleapis.com/css2?family=Raleway&display=swap" rel="stylesheet"><!--<![endif]-->
            <style type="text/css">
                #outlook a {
                    padding: 0;
                }

                .es-button {
                    mso-style-priority: 100 !important;
                    text-decoration: none !important;
                }

                a[x-apple-data-detectors] {
                    color: inherit !important;
                    text-decoration: none !important;
                    font-size: inherit !important;
                    font-family: inherit !important;
                    font-weight: inherit !important;
                    line-height: inherit !important;
                }

                .es-desk-hidden {
                    display: none;
                    float: left;
                    overflow: hidden;
                    width: 0;
                    max-height: 0;
                    line-height: 0;
                    mso-hide: all;
                }

                @media only screen and (max-width:600px) {

                    p,
                    ul li,
                    ol li,
                    a {
                        line-height: 150% !important
                    }

                    h1,
                    h2,
                    h3,
                    h1 a,
                    h2 a,
                    h3 a {
                        line-height: 120%
                    }

                    h1 {
                        font-size: 40px !important;
                        text-align: center !important
                    }

                    h2 {
                        font-size: 32px !important;
                        text-align: center !important
                    }

                    h3 {
                        font-size: 24px !important;
                        text-align: center !important
                    }

                    .es-header-body h1 a,
                    .es-content-body h1 a,
                    .es-footer-body h1 a {
                        font-size: 40px !important;
                        text-align: center !important
                    }

                    .es-header-body h2 a,
                    .es-content-body h2 a,
                    .es-footer-body h2 a {
                        font-size: 32px !important;
                        text-align: center !important
                    }

                    .es-header-body h3 a,
                    .es-content-body h3 a,
                    .es-footer-body h3 a {
                        font-size: 24px !important;
                        text-align: center !important
                    }

                    .es-menu td a {
                        font-size: 12px !important
                    }

                    .es-header-body p,
                    .es-header-body ul li,
                    .es-header-body ol li,
                    .es-header-body a {
                        font-size: 14px !important
                    }

                    .es-content-body p,
                    .es-content-body ul li,
                    .es-content-body ol li,
                    .es-content-body a {
                        font-size: 14px !important
                    }

                    .es-footer-body p,
                    .es-footer-body ul li,
                    .es-footer-body ol li,
                    .es-footer-body a {
                        font-size: 12px !important
                    }

                    .es-infoblock p,
                    .es-infoblock ul li,
                    .es-infoblock ol li,
                    .es-infoblock a {
                        font-size: 12px !important
                    }

                    *[class="gmail-fix"] {
                        display: none !important
                    }

                    .es-m-txt-c,
                    .es-m-txt-c h1,
                    .es-m-txt-c h2,
                    .es-m-txt-c h3 {
                        text-align: center !important
                    }

                    .es-m-txt-r,
                    .es-m-txt-r h1,
                    .es-m-txt-r h2,
                    .es-m-txt-r h3 {
                        text-align: right !important
                    }

                    .es-m-txt-l,
                    .es-m-txt-l h1,
                    .es-m-txt-l h2,
                    .es-m-txt-l h3 {
                        text-align: left !important
                    }

                    .es-m-txt-r img,
                    .es-m-txt-c img,
                    .es-m-txt-l img {
                        display: inline !important
                    }

                    .es-button-border {
                        display: inline-block !important
                    }

                    a.es-button,
                    button.es-button {
                        font-size: 16px !important;
                        display: inline-block !important
                    }

                    .es-adaptive table,
                    .es-left,
                    .es-right {
                        width: 100% !important
                    }

                    .es-content table,
                    .es-header table,
                    .es-footer table,
                    .es-content,
                    .es-footer,
                    .es-header {
                        width: 100% !important;
                        max-width: 600px !important
                    }

                    .es-adapt-td {
                        display: block !important;
                        width: 100% !important
                    }

                    .adapt-img {
                        width: 100% !important;
                        height: auto !important
                    }

                    .es-m-p0 {
                        padding: 0 !important
                    }

                    .es-m-p0r {
                        padding-right: 0 !important
                    }

                    .es-m-p0l {
                        padding-left: 0 !important
                    }

                    .es-m-p0t {
                        padding-top: 0 !important
                    }

                    .es-m-p0b {
                        padding-bottom: 0 !important
                    }

                    .es-m-p20b {
                        padding-bottom: 20px !important
                    }

                    .es-mobile-hidden,
                    .es-hidden {
                        display: none !important
                    }

                    tr.es-desk-hidden,
                    td.es-desk-hidden,
                    table.es-desk-hidden {
                        width: auto !important;
                        overflow: visible !important;
                        float: none !important;
                        max-height: inherit !important;
                        line-height: inherit !important
                    }

                    tr.es-desk-hidden {
                        display: table-row !important
                    }

                    table.es-desk-hidden {
                        display: table !important
                    }

                    td.es-desk-menu-hidden {
                        display: table-cell !important
                    }

                    .es-menu td {
                        width: 1% !important
                    }

                    table.es-table-not-adapt,
                    .esd-block-html table {
                        width: auto !important
                    }

                    table.es-social {
                        display: inline-block !important
                    }

                    table.es-social td {
                        display: inline-block !important
                    }

                    .es-desk-hidden {
                        display: table-row !important;
                        width: auto !important;
                        overflow: visible !important;
                        max-height: inherit !important
                    }

                    .es-m-p5 {
                        padding: 5px !important
                    }

                    .es-m-p5t {
                        padding-top: 5px !important
                    }

                    .es-m-p5b {
                        padding-bottom: 5px !important
                    }

                    .es-m-p5r {
                        padding-right: 5px !important
                    }

                    .es-m-p5l {
                        padding-left: 5px !important
                    }

                    .es-m-p10 {
                        padding: 10px !important
                    }

                    .es-m-p10t {
                        padding-top: 10px !important
                    }

                    .es-m-p10b {
                        padding-bottom: 10px !important
                    }

                    .es-m-p10r {
                        padding-right: 10px !important
                    }

                    .es-m-p10l {
                        padding-left: 10px !important
                    }

                    .es-m-p15 {
                        padding: 15px !important
                    }

                    .es-m-p15t {
                        padding-top: 15px !important
                    }

                    .es-m-p15b {
                        padding-bottom: 15px !important
                    }

                    .es-m-p15r {
                        padding-right: 15px !important
                    }

                    .es-m-p15l {
                        padding-left: 15px !important
                    }

                    .es-m-p20 {
                        padding: 20px !important
                    }

                    .es-m-p20t {
                        padding-top: 20px !important
                    }

                    .es-m-p20r {
                        padding-right: 20px !important
                    }

                    .es-m-p20l {
                        padding-left: 20px !important
                    }

                    .es-m-p25 {
                        padding: 25px !important
                    }

                    .es-m-p25t {
                        padding-top: 25px !important
                    }

                    .es-m-p25b {
                        padding-bottom: 25px !important
                    }

                    .es-m-p25r {
                        padding-right: 25px !important
                    }

                    .es-m-p25l {
                        padding-left: 25px !important
                    }

                    .es-m-p30 {
                        padding: 30px !important
                    }

                    .es-m-p30t {
                        padding-top: 30px !important
                    }

                    .es-m-p30b {
                        padding-bottom: 30px !important
                    }

                    .es-m-p30r {
                        padding-right: 30px !important
                    }

                    .es-m-p30l {
                        padding-left: 30px !important
                    }

                    .es-m-p35 {
                        padding: 35px !important
                    }

                    .es-m-p35t {
                        padding-top: 35px !important
                    }

                    .es-m-p35b {
                        padding-bottom: 35px !important
                    }

                    .es-m-p35r {
                        padding-right: 35px !important
                    }

                    .es-m-p35l {
                        padding-left: 35px !important
                    }

                    .es-m-p40 {
                        padding: 40px !important
                    }

                    .es-m-p40t {
                        padding-top: 40px !important
                    }

                    .es-m-p40b {
                        padding-bottom: 40px !important
                    }

                    .es-m-p40r {
                        padding-right: 40px !important
                    }

                    .es-m-p40l {
                        padding-left: 40px !important
                    }
                }
            </style>
        </head>

        <body data-new-gr-c-s-loaded="9.69.0"
            style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0">
            <div class="es-wrapper-color" style="background-color:#EFF7F6"><!--[if gte mso 9]>
        <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
        <v:fill type="tile" color="#eff7f6"></v:fill>
        </v:background>
        <![endif]-->
                <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0"
                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top;background-color:#EFF7F6">
                    <tr>
                        <td valign="top" style="padding:0;Margin:0">
                            <table cellpadding="0" cellspacing="0" class="es-header" align="center"
                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top">
                                <tr>
                                    <td align="center" style="padding:0;Margin:0">
                                        <table bgcolor="#ffffff" class="es-header-body" align="center" cellpadding="0"
                                            cellspacing="0"
                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;width:600px">
                                            <tr>
                                                <td class="es-m-p0b" align="left" style="padding:20px;Margin:0">
                                                    <!--[if mso]><table style="width:560px" cellpadding="0" cellspacing="0"><tr><td style="width:281px" valign="top"><![endif]-->
                                                    <table cellpadding="0" cellspacing="0" class="es-left" align="left"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left">
                                                        <tr>
                                                            <td class="es-m-p0r es-m-p20b" valign="top" align="center"
                                                                style="padding:0;Margin:0;width:261px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="left" class="es-m-txt-c"
                                                                            style="padding:0;Margin:0;padding-top:5px;padding-bottom:5px;font-size:0px">
                                                                            <img src="https://api.kumpeapps.com/images/kumpeapps/base_logo_white_background.png"
                                                                                alt="Logo"
                                                                                style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;font-size:12px"
                                                                                height="45" title="Logo"></td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                            <td class="es-hidden" style="padding:0;Margin:0;width:20px"></td>
                                                        </tr>
                                                    </table><!--[if mso]></td><td style="width:128px" valign="top"><![endif]-->
                                                    <table cellpadding="0" cellspacing="0" class="es-left" align="left"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left">
                                                        <tr>
                                                            <td align="left" class="es-m-p20b"
                                                                style="padding:0;Margin:0;width:128px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="center"
                                                                            style="padding:0;Margin:0;display:none"></td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <!--[if mso]></td><td style="width:20px"></td><td style="width:131px" valign="top"><![endif]-->
                                                    <table cellpadding="0" cellspacing="0" class="es-right" align="right"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right">
                                                        <tr class="es-mobile-hidden">
                                                            <td align="left" style="padding:0;Margin:0;width:131px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="center"
                                                                            style="padding:0;Margin:0;padding-top:10px"><!--[if mso]><a href="https://support.kumpeapps.com" target="_blank" hidden>
        <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" esdevVmlButton href="https://support.kumpeapps.com"
        style="height:39px; v-text-anchor:middle; width:122px" arcsize="13%" strokecolor="#386641" strokeweight="1px" fillcolor="#6a994e">
        <w:anchorlock></w:anchorlock>
        <center style='color:#ffffff; font-family:Raleway, Arial, sans-serif; font-size:14px; font-weight:400; line-height:14px; mso-text-raise:1px'>Support</center>
        </v:roundrect></a>
        <![endif]--><!--[if !mso]><!-- --><span class="msohide es-button-border"
                                                                                style="border-style:solid;border-color:#386641;background:#6A994E;border-width:1px;display:inline-block;border-radius:5px;width:auto;mso-hide:all"><a
                                                                                    href="https://support.kumpeapps.com"
                                                                                    class="es-button" target="_blank"
                                                                                    style="mso-style-priority:100 !important;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#FFFFFF;font-size:16px;display:inline-block;background:#6A994E;border-radius:5px;font-family:Raleway, Arial, sans-serif;font-weight:normal;font-style:normal;line-height:19px;width:auto;text-align:center;padding:10px 30px 10px 30px;mso-padding-alt:0;mso-border-alt:10px solid #6A994E">Support</a></span><!--<![endif]-->
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table><!--[if mso]></td></tr></table><![endif]-->
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                            <table class="es-content" cellspacing="0" cellpadding="0" align="center"
                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
                                <tr>
                                    <td align="center" style="padding:0;Margin:0">
                                        <table class="es-content-body"
                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#ffffff;width:600px"
                                            cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center">
                                            <tr>
                                                <td align="left" style="padding:0;Margin:0">
                                                    <table cellspacing="0" cellpadding="0" width="100%"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr>
                                                            <td class="es-m-p0r" valign="top" align="center"
                                                                style="padding:0;Margin:0;width:600px">
                                                                <table width="100%" cellspacing="0" cellpadding="0"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="center"
                                                                            style="padding:0;Margin:0;position:relative"><img
                                                                                class="adapt-img"
                                                                                src="https://fcfevie.stripocdn.email/content/guids/bannerImgGuid/images/image16967259761608780.png"
                                                                                alt title width="600"
                                                                                style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic">
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td align="left" bgcolor="#6a994e"
                                                    style="Margin:0;padding-left:20px;padding-right:20px;padding-top:30px;padding-bottom:30px;background-color:#6a994e">
                                                    <table cellpadding="0" cellspacing="0" width="100%"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr>
                                                            <td align="center" valign="top"
                                                                style="padding:0;Margin:0;width:560px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="center" class="es-m-txt-c"
                                                                            style="padding:10px;Margin:0">
                                                                            <h3
                                                                                style="Margin:0;line-height:29px;mso-line-height-rule:exactly;font-family:Raleway, Arial, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#ffffff">
                                                                                Hello email_name,</h3>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td align="center" class="es-m-txt-c"
                                                                            style="padding:0;Margin:0;padding-top:20px">
                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;line-height:24px;color:#ffffff;font-size:16px">
                                                                                Thank you for your recent order. We are pleased
                                                                                to confirm that we have received your order and
                                                                                it is currently being processed.</p>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td align="center" style="padding:0;Margin:0;font-size:0px"><a target="_blank"
                                                                        href=""
                                                                        style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:underline;color:#6A994E;font-size:16px"><img
                                                                            class="adapt-img p_image"
                                                                            src="email_base_url/order_status_image?order_id=email_orderid"
                                                                            alt
                                                                            style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;border-radius:10px"
                                                                            width="75%"></a></td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                            <table cellpadding="0" cellspacing="0" class="es-content" align="center"
                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
                                <tr>
                                    <td align="center" style="padding:0;Margin:0">
                                        <table bgcolor="#ffffff" class="es-content-body" align="center" cellpadding="0"
                                            cellspacing="0"
                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;width:600px">
                                            <tr>
                                                <td align="left"
                                                    style="Margin:0;padding-left:20px;padding-right:20px;padding-bottom:30px;padding-top:40px">
                                                    <table cellpadding="0" cellspacing="0" width="100%"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr>
                                                            <td align="center" valign="top"
                                                                style="padding:0;Margin:0;width:560px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="center" style="padding:0;Margin:0">
                                                                            <h1
                                                                                style="Margin:0;line-height:60px;mso-line-height-rule:exactly;font-family:Raleway, Arial, sans-serif;font-size:50px;font-style:normal;font-weight:normal;color:#386641">
                                                                                Order summary</h1>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td align="center" class="es-m-p10t"
                                                                            style="padding:0;Margin:0;padding-left:20px;padding-right:20px;padding-top:40px">
                                                                            <h3 class="b_title"
                                                                                style="Margin:0;line-height:29px;mso-line-height-rule:exactly;font-family:Raleway, Arial, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#386641">
                                                                                ORDER NO.&nbsp;email_orderid<br>email_date</h3>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            
                                            email_products

                                            <tr>
                                                <td align="left"
                                                    style="Margin:0;padding-left:20px;padding-right:20px;padding-bottom:30px;padding-top:40px">
                                                    <table cellpadding="0" cellspacing="0" width="100%"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr>
                                                            <td align="center" valign="top"
                                                                style="padding:0;Margin:0;width:560px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="center" style="padding:0;Margin:0">
                                                                            <h1
                                                                                style="Margin:0;line-height:60px;mso-line-height-rule:exactly;font-family:Raleway, Arial, sans-serif;font-size:50px;font-style:normal;font-weight:normal;color:#386641">
                                                                                Order total</h1>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td class="esdev-adapt-off" align="left" style="padding:20px;Margin:0">
                                                    <table cellpadding="0" cellspacing="0" class="esdev-mso-table"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;width:560px">
                                                        <tr>
                                                            <td class="esdev-mso-td" valign="top" style="padding:0;Margin:0">
                                                                <table cellpadding="0" cellspacing="0" class="es-left"
                                                                    align="left"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left">
                                                                    <tr>
                                                                        <td align="left" style="padding:0;Margin:0;width:270px">
                                                                            <table cellpadding="0" cellspacing="0" width="100%"
                                                                                role="presentation"
                                                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                                <tr>
                                                                                    <td align="left" style="padding:0;Margin:0">
                                                                                        <p
                                                                                            style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;line-height:24px;color:#4D4D4D;font-size:16px">
                                                                                            Subtotal<br>Shipping<br>Taxes</p>
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                            <td style="padding:0;Margin:0;width:20px"></td>
                                                            <td class="esdev-mso-td" valign="top" style="padding:0;Margin:0">
                                                                <table cellpadding="0" cellspacing="0" class="es-right"
                                                                    align="right"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right">
                                                                    <tr>
                                                                        <td align="left" style="padding:0;Margin:0;width:270px">
                                                                            <table cellpadding="0" cellspacing="0" width="100%"
                                                                                role="presentation"
                                                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                                <tr>
                                                                                    <td align="right"
                                                                                        style="padding:0;Margin:0">
                                                                                        <p
                                                                                            style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;line-height:24px;color:#4D4D4D;font-size:16px">
                                                                                            email_subtotal<br>email_shippingcost<br>email_taxes</p>
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td align="left"
                                                    style="padding:0;Margin:0;padding-left:20px;padding-right:20px">
                                                    <table cellpadding="0" cellspacing="0" width="100%"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr>
                                                            <td align="center" valign="top"
                                                                style="padding:0;Margin:0;width:560px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="center"
                                                                            style="padding:0;Margin:0;padding-top:5px;padding-bottom:5px;font-size:0">
                                                                            <table border="0" width="100%" height="100%"
                                                                                cellpadding="0" cellspacing="0"
                                                                                role="presentation"
                                                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                                <tr>
                                                                                    <td
                                                                                        style="padding:0;Margin:0;border-bottom:5px dotted #a7c957;background:unset;height:1px;width:100%;margin:0px">
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td class="esdev-adapt-off" align="left" style="padding:20px;Margin:0">
                                                    <table cellpadding="0" cellspacing="0" class="esdev-mso-table"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;width:560px">
                                                        <tr>
                                                            <td class="esdev-mso-td" valign="top" style="padding:0;Margin:0">
                                                                <table cellpadding="0" cellspacing="0" class="es-left"
                                                                    align="left"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left">
                                                                    <tr>
                                                                        <td align="left" style="padding:0;Margin:0;width:270px">
                                                                            <table cellpadding="0" cellspacing="0" width="100%"
                                                                                role="presentation"
                                                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                                <tr>
                                                                                    <td align="left" class="es-m-txt-l"
                                                                                        style="padding:0;Margin:0">
                                                                                        <h3
                                                                                            style="Margin:0;line-height:29px;mso-line-height-rule:exactly;font-family:Raleway, Arial, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#386641">
                                                                                            Total</h3>
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                            <td style="padding:0;Margin:0;width:20px"></td>
                                                            <td class="esdev-mso-td" valign="top" style="padding:0;Margin:0">
                                                                <table cellpadding="0" cellspacing="0" class="es-right"
                                                                    align="right"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right">
                                                                    <tr>
                                                                        <td align="left" style="padding:0;Margin:0;width:270px">
                                                                            <table cellpadding="0" cellspacing="0" width="100%"
                                                                                role="presentation"
                                                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                                <tr>
                                                                                    <td align="right" class="es-m-txt-r"
                                                                                        style="padding:0;Margin:0">
                                                                                        <h3
                                                                                            style="Margin:0;line-height:29px;mso-line-height-rule:exactly;font-family:Raleway, Arial, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#386641">
                                                                                            email_total</h3><br>
                                                                                            <b>Order Notes:</b> email_notes
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td align="left"
                                                    style="Margin:0;padding-left:20px;padding-right:20px;padding-bottom:30px;padding-top:40px">
                                                    <table cellpadding="0" cellspacing="0" width="100%"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr>
                                                            <td align="center" valign="top"
                                                                style="padding:0;Margin:0;width:560px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="center" style="padding:0;Margin:0">
                                                                            <h1
                                                                                style="Margin:0;line-height:60px;mso-line-height-rule:exactly;font-family:Raleway, Arial, sans-serif;font-size:50px;font-style:normal;font-weight:normal;color:#386641">
                                                                                Shipping</h1>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td align="left" style="padding:20px;Margin:0">
                                                    <!--[if mso]><table style="width:560px" cellpadding="0" cellspacing="0"><tr><td style="width:270px" valign="top"><![endif]-->
                                                    <table cellpadding="0" cellspacing="0" class="es-left" align="left"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left">
                                                        <tr>
                                                            <td class="es-m-p20b" align="left"
                                                                style="padding:0;Margin:0;width:270px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="left" style="padding:0;Margin:0">
                                                                            <h3
                                                                                style="Margin:0;line-height:29px;mso-line-height-rule:exactly;font-family:Raleway, Arial, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#386641">
                                                                                Shipping Address</h3>
                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;line-height:24px;color:#4D4D4D;font-size:16px">
                                                                                email_shippingname<br>
                                                                                email_address<br>
                                                                                email_city, email_state  email_zip<br>
                                                                                email_country</p>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td align="left" style="padding:20px;Margin:0">
                                                    <!--[if mso]><table style="width:560px" cellpadding="0" cellspacing="0"><tr><td style="width:270px" valign="top"><![endif]-->
                                                    <table cellpadding="0" cellspacing="0" class="es-left" align="left"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left">
                                                        <tr>
                                                            <td class="es-m-p20b" align="left"
                                                                style="padding:0;Margin:0;width:270px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="left" style="padding:0;Margin:0">
                                                                            <h3
                                                                                style="Margin:0;line-height:29px;mso-line-height-rule:exactly;font-family:Raleway, Arial, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#386641">
                                                                                Payment&nbsp;Method</h3>
                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;line-height:24px;color:#4D4D4D;font-size:16px">
                                                                                email_paymentmethod</p>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <!--[if mso]></td><td style="width:20px"></td><td style="width:270px" valign="top"><![endif]-->
                                                    <table cellpadding="0" cellspacing="0" class="es-right" align="right"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right">
                                                        <tr>
                                                            <td align="left" style="padding:0;Margin:0;width:270px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="left" style="padding:0;Margin:0">
                                                                            <h3
                                                                                style="Margin:0;line-height:29px;mso-line-height-rule:exactly;font-family:Raleway, Arial, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#386641">
                                                                                Shipping Method</h3>
                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;line-height:24px;color:#4D4D4D;font-size:16px">
                                                                                email_shippingmethod</p>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table><!--[if mso]></td></tr></table><![endif]-->
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                            <table cellpadding="0" cellspacing="0" class="es-content" align="center"
                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
                                <tr>
                                    <td align="center" style="padding:0;Margin:0">
                                        <table bgcolor="#ffffff" class="es-content-body" align="center" cellpadding="0"
                                            cellspacing="0"
                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;width:600px">
                                            <tr>
                                                <td align="left"
                                                    style="Margin:0;padding-bottom:20px;padding-left:20px;padding-right:20px;padding-top:40px">
                                                    <table cellpadding="0" cellspacing="0" width="100%"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr>
                                                            <td align="center" valign="top"
                                                                style="padding:0;Margin:0;width:560px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="center" style="padding:0;Margin:0">
                                                                            <h1
                                                                                style="Margin:0;line-height:60px;mso-line-height-rule:exactly;font-family:Raleway, Arial, sans-serif;font-size:50px;font-style:normal;font-weight:normal;color:#386641">
                                                                                Shop information</h1>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td align="left"
                                                    style="padding:0;Margin:0;padding-left:20px;padding-right:20px">
                                                    <table cellpadding="0" cellspacing="0" width="100%"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr>
                                                            <td align="center" valign="top"
                                                                style="padding:0;Margin:0;width:560px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="center"
                                                                            style="padding:0;Margin:0;padding-top:5px;padding-bottom:5px;font-size:0">
                                                                            <table border="0" width="100%" height="100%"
                                                                                cellpadding="0" cellspacing="0"
                                                                                role="presentation"
                                                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                                <tr>
                                                                                    <td
                                                                                        style="padding:0;Margin:0;border-bottom:5px dotted #a7c957;background:unset;height:1px;width:100%;margin:0px">
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td class="esdev-adapt-off" align="left" style="padding:20px;Margin:0">
                                                    <table cellpadding="0" cellspacing="0" width="100%"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr>
                                                            <td align="left" style="padding:0;Margin:0;width:560px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="left"
                                                                            style="padding:0;Margin:0;padding-top:10px">
                                                                            <h3 class="b_description"
                                                                                style="Margin:0;line-height:29px;mso-line-height-rule:exactly;font-family:Raleway, Arial, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#386641">
                                                                                Shipping<br></h3><br>
                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;line-height:24px;color:#4D4D4D;font-size:16px">
                                                                                <strong>Customs and import taxes</strong></p>
                                                                            Buyers are responsible for any customs and import
                                                                            taxes that may apply. Sellers aren't responsible for
                                                                            delays due to customs.<br><br>
                                                                            <h3
                                                                                style="Margin:0;line-height:29px;mso-line-height-rule:exactly;font-family:Raleway, Arial, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#386641">
                                                                                Returns and exchanges</h3>
                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;line-height:24px;color:#4D4D4D;font-size:16px">
                                                                                <br></p>
                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;line-height:24px;color:#4D4D4D;font-size:16px">
                                                                                <strong>All orders are final</strong></p>
                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;line-height:24px;color:#4D4D4D;font-size:16px">
                                                                                If the order arrived damaged or not as described
                                                                                please email us at sales@kumpeapps.com and we
                                                                                will do what we can to make it right.<br><br>
                                                                            </p>
                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;line-height:24px;color:#4D4D4D;font-size:16px">
                                                                                <strong
                                                                                    style="color:#4d4d4d;font-family:tahoma, verdana, segoe, sans-serif;font-size:16px;text-align:center">Conditions
                                                                                    of return</strong></p>
                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;line-height:24px;color:#4D4D4D;font-size:16px">
                                                                                Buyers are responsible for return shipping
                                                                                costs. If the item is not returned in its
                                                                                original condition, the buyer is responsible for
                                                                                any loss in value.</p>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td align="left"
                                                    style="padding:0;Margin:0;padding-left:20px;padding-right:20px;padding-bottom:40px">
                                                    <table cellpadding="0" cellspacing="0" width="100%"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr>
                                                            <td align="center" valign="top"
                                                                style="padding:0;Margin:0;width:560px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="center"
                                                                            style="padding:0;Margin:0;padding-top:5px;padding-bottom:5px;font-size:0">
                                                                            <table border="0" width="100%" height="100%"
                                                                                cellpadding="0" cellspacing="0"
                                                                                role="presentation"
                                                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                                <tr>
                                                                                    <td
                                                                                        style="padding:0;Margin:0;border-bottom:5px dotted #a7c957;background:unset;height:1px;width:100%;margin:0px">
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                            <table cellpadding="0" cellspacing="0" class="es-footer" align="center"
                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top">
                                <tr>
                                    <td align="center" style="padding:0;Margin:0">
                                        <table bgcolor="#ffffff" class="es-footer-body" align="center" cellpadding="0"
                                            cellspacing="0"
                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;width:600px">
                                            <tr>
                                                <td align="left" style="padding:0;Margin:0">
                                                    <table cellpadding="0" cellspacing="0" width="100%"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr>
                                                            <td align="center" valign="top"
                                                                style="padding:0;Margin:0;width:600px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="center"
                                                                            style="padding:0;Margin:0;padding-top:5px;padding-bottom:5px;font-size:0">
                                                                            <table border="0" width="100%" height="100%"
                                                                                cellpadding="0" cellspacing="0"
                                                                                role="presentation"
                                                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                                <tr>
                                                                                    <td
                                                                                        style="padding:0;Margin:0;border-bottom:2px solid #eff7f6;background:unset;height:1px;width:100%;margin:0px">
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td align="left"
                                                    style="Margin:0;padding-left:20px;padding-right:20px;padding-top:30px;padding-bottom:30px">
                                                    <table cellpadding="0" cellspacing="0" width="100%"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr>
                                                            <td align="left" style="padding:0;Margin:0;width:560px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="center" class="es-m-txt-c"
                                                                            style="padding:0;Margin:0;padding-bottom:20px;font-size:0px">
                                                                            <a target="_blank" href=""
                                                                                style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:underline;color:#6A994E;font-size:12px"><img
                                                                                    src="https://api.kumpeapps.com/images/kumpeapps/base_logo_white_background.png"
                                                                                    alt="Logo"
                                                                                    style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic"
                                                                                    title="Logo" height="50"></a></td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td align="center" style="padding:0;Margin:0">
                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:tahoma, verdana, segoe, sans-serif;line-height:20px;color:#4D4D4D;font-size:13px">
                                                                                <a target="_blank"
                                                                                    style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;color:#6A994E;font-size:12px"
                                                                                    href=""></a><a target="_blank"
                                                                                    style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;color:#6A994E;font-size:12px"
                                                                                    href="https://app.termly.io/document/privacy-policy/cb1b4a7a-f0fa-4bb1-a521-c20bd2349dc4">Privacy
                                                                                    Policy</a></p>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                            <table cellpadding="0" cellspacing="0" class="es-content" align="center"
                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
                                <tr>
                                    <td align="center" style="padding:0;Margin:0">
                                        <table class="es-content-body" align="center" cellpadding="0" cellspacing="0"
                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:600px">
                                            <tr>
                                                <td align="left" style="padding:20px;Margin:0">
                                                    <table cellpadding="0" cellspacing="0" width="100%"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr>
                                                            <td align="center" valign="top"
                                                                style="padding:0;Margin:0;width:560px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                    <tr>
                                                                        <td align="center"
                                                                            style="padding:0;Margin:0;display:none"></td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </div>
        </body>

        </html>
    """

    for key in data:
        value = data[key]
        html_email = html_email.replace(key, f'{value}')
    return html_email

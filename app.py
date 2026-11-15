import streamlit as st
import pandas as pd
from datetime import date
from io import BytesIO

st.set_page_config(page_title="النظام المحاسبي الذكي - أخصائي الإيرادات", layout="wide")

st.title("📊 نظام أخصائي المحاسبة والإيرادات الذكي")
st.write("نظام محاسبي متكامل مبني وفق الأصول المحاسبية مع لوحة تحكم ذكية للتحليل المالي وتتبع القيود المزدوجة.")

# تهيئة الذاكرة لحفظ شجرة الحسابات والقيود المالية
if 'chart_of_accounts' not in st.session_state:
    st.session_state.chart_of_accounts = [
        {"رمز الحساب": "101", "اسم الحساب": "الصندوق / النقدية", "النوع": "أصول"},
        {"رمز الحساب": "102", "اسم الحساب": "البنك", "النوع": "أصول"},
        {"رمز الحساب": "201", "اسم الحساب": "الموردين / الدائنون", "النوع": "خصوم"},
        {"رمز الحساب": "401", "اسم الحساب": "إيرادات الخدمات الطبية / المبيعات", "النوع": "إيرادات"},
        {"رمز الحساب": "501", "اسم الحساب": "المصروفات التشغيلية والرواتب", "النوع": "مصروفات"}
    ]

if 'journal_entries' not in st.session_state:
    st.session_state.journal_entries = pd.DataFrame(columns=[
        'رقم القيد', 'التاريخ', 'رقم الحساب (مدين)', 'مدين (ريال)', 
        'رقم الحساب (دائن)', 'دائن (ريال)', 'الوصف / البيان'
    ])

# القائمة الجانبية للعمليات المحاسبية
st.sidebar.header("⚙️ العمليات المحاسبية")
menu = st.sidebar.selectbox("اختر القسم", ["إدخال قيد محاسبي مزدوج", "إدارة شجرة الحسابات", "عرض التقارير وقائمة الدخل"])

# 1. إدخال القيد المحاسبي (نظام مدين ودائن)
if menu == "إدخال قيد محاسبي مزدوج":
    st.header("📝 تسجيل قيد محاسبي جديد (مدين ودائن)")
    
    # تجهيز أسماء الحسابات للاختيار
    accounts_list = [f"{acc['رمز الحساب']} - {acc['اسم الحساب']}" for acc in st.session_state.chart_of_accounts]
    
    with st.form("entry_form"):
        col1, col2 = st.columns(2)
        with col1:
            e_date = st.date_input("تاريخ القيد", date.today())
            debit_account = st.selectbox("الحساب المدين (من ح/)", accounts_list)
            debit_amount = st.number_input("المبلغ المدين (ريال)", min_value=0.0, step=10.0, format="%.2f")
            
        with col2:
            entry_id = st.number_input("رقم القيد", min_value=1, step=1, value=len(st.session_state.journal_entries)+1)
            credit_account = st.selectbox("الحساب الدائن (إلى ح/)", accounts_list)
            credit_amount = st.number_input("المبلغ الدائن (ريال)", min_value=0.0, step=10.0, format="%.2f")
            
        description = st.text_area("البيان / شرح القيد المحاسبي")
        
        submit_entry = st.form_submit_button(label="اعتماد وحفظ القيد المحاسبي")
        
        if submit_entry:
            if debit_amount != credit_amount:
                st.error("❌ خطأ محاسبي: يجب أن يتطابق المبلغ المدين مع المبلغ الدائن تماماً!")
            elif debit_amount <= 0:
                st.error("❌ يجيب أن يكون المبلغ أكبر من الصفر.")
            else:
                new_entry = pd.DataFrame({
                    'رقم القيد': [entry_id],
                    'التاريخ': [e_date],
                    'رقم الحساب (مدين)': [debit_account],
                    'مدين (ريال)': [debit_amount],
                    'رقم الحساب (دائن)': [credit_account],
                    'دائن (ريال)': [credit_amount],
                    'الوصف / البيان': [description]
                })
                st.session_state.journal_entries = pd.concat([st.session_state.journal_entries, new_entry], ignore_index=True)
                st.success("✅ تم تسجيل القيد المحاسبي وترحيله بنجاح!")

    st.markdown("---")
    st.subheader("دفتر اليومية العامة")
    if not st.session_state.journal_entries.empty:
        st.dataframe(st.session_state.journal_entries, use_container_width=True)
    else:
        st.info("لا توجد قيود مسجلة حتى الآن.")

# 2. شجرة الحسابات
elif menu == "إدارة شجرة الحسابات":
    st.header("🌳 شجرة الحسابات المحاسبية")
    st.write("هذه الحسابات الأساسية المعرّفة في النظام:")
    
    df_accounts = pd.DataFrame(st.session_state.chart_of_accounts)
    st.dataframe(df_accounts, use_container_width=True)
    
    with st.form("add_account"):
        st.subheader("إضافة حساب جديد للشجرة")
        new_code = st.text_input("رمز الحساب (مثال: 103 أو 402)")
        new_name = st.text_input("اسم الحساب")
        new_type = st.selectbox("نوع الحساب", ["أصول", "خصوم", "إيرادات", "مصروفات"])
        add_acc_btn = st.form_submit_button("إضافة الحساب")
        
        if add_acc_btn and new_code and new_name:
            st.session_state.chart_of_accounts.append({"رمز الحساب": new_code, "اسم الحساب": new_name, "نوع الحساب": new_type})
            st.success(f"تمت إضافة الحساب {new_name} بنجاح!")
            st.rerun()

# 3. التقارير المالية وقائمة الدخل وتحليل الذكاء الاصطناعي المالي
elif menu == "عرض التقارير وقائمة الدخل":
    st.header("📈 التقارير المالية وقائمة الدخل الذكية")
    
    df = st.session_state.journal_entries
    
    if not df.empty:
        # حساب إجمالي الإيرادات والمصروفات بناء على الكلمات المفتاحية في الحسابات أو المدخلات
        total_revenues = df[df['رقم الحساب (دائن)'].str.contains("إيرادات|مبيعات", na=False)]['دائن (ريال)'].sum()
        total_expenses = df[df['رقم الحساب (مدين)'].str.contains("مصروفات|رواتب", na=False)]['مدين (ريال)'].sum()
        
        # لو اعتبرنا المبالغ الإجمالية تقريبية بناء على الحركات
        net_profit = total_revenues - total_expenses
        
        col1, col2, col3 = st.columns(3)
        col1.metric("إجمالي الإيرادات المسجلة", f"{total_revenues:,.2f} ريال")
        col2.metric("إجمالي المصروفات التشغيلية", f"{total_expenses:,.2f} ريال")
        col3.metric("صافي الربح / (الخسارة)", f"{net_profit:,.2f} ريال", delta=f"{net_profit:,.2f}")
        
        st.markdown("---")
        st.subheader("🤖 التحليل المالي الذكي (AI Financial Advisor)")
        
        # محرك تحليل ذكي يقرا الأرقام ويعطي توصيات تلقائية
        if total_revenues > 0 or total_expenses > 0:
            ai_insight = ""
            if net_profit > 0:
                ai_insight = f"🟢 **مؤشر إيجابي:** الأداء المالي ممتاز؛ صافي الدخل يحقق ربحية بـ {net_profit:,.2f} ريال. يُنصح بتخصيص نسبة (10-15%) للاحتياطي التشغيلي وتنمية الإيرادات."
            elif net_profit == 0:
                ai_insight = "🟡 **تنبيه تعادل:** الإيرادات تغطي المصروفات تماماً دون وجود هامش ربح صافي. راجع بنود المصروفات التشغيلية."
            else:
                ai_insight = f"🔴 **تنبيه عجز مالي:** المصروفات أعلى من الإيرادات بمقدار الصافي السالب ({net_profit:,.2f} ريال). يجب إعادة هيكلة المصروفات والتركيز على قنوات تنمية الإيرادات بسرعة."
            
            st.info(ai_insight)
        else:
            st.info("أدخل قيود مالية لإظهار التحليل الذكي.")
            
        st.markdown("---")
        st.subheader("📥 تصدير التقارير المالية")
        
        def to_excel(df_data):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df_data.to_excel(writer, index=False, sheet_name='القيود المحاسبية')
            return output.getvalue()

        excel_file = to_excel(df)
        st.download_button(
            label="📥 تحميل دفتر اليومية كامل بصيغة Excel",
            data=excel_file,
            file_name=f"accounting_ledger_{date.today()}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        
        if st.button("🗑️ تصفير ومسح كافة القيود المحاسبية"):
            st.session_state.journal_entries = pd.DataFrame(columns=[
                'رقم القيد', 'التاريخ', 'رقم الحساب (مدين)', 'مدين (ريال)', 
                'رقم الحساب (دائن)', 'دائن (ريال)', 'الوصف / البيان'
            ])
            st.rerun()
    else:
        st.warning("⚠️ لا توجد قيود مالية مسجلة بعد لعرض التقارير. انتقل لصفحة 'إدخال قيد محاسبي' وابدأ بإدخال حركاتك.")
